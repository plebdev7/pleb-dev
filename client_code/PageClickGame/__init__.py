from math import floor, ceil, log2

from ._anvil_designer import PageClickGameTemplate  # type: ignore
from .ClickGame import CG, TAB, STATE
from .Generator import Generators
from .State import activate_state
from .Tab import Tabs
from .Upgrade import CoreUpgrades, ClickUpgrades

from ..Utilities import dispnum

# from anvil import *


class PageClickGame(PageClickGameTemplate):
    TITLE = 'click'
    
    def __init__(self, **properties):
        self.init_components(**properties)
        CG.game = self
        
        # setup timer
        self.timer.interval = CG.tick_time

        # set tab button
        self.button_generators.tag.tab = TAB.GENERATORS
        self.button_auto_clicker.tag.tab = TAB.AUTO_CLICKER
        self.button_clickometer.tag.tab = TAB.CLICKOMETER
        self.tab_buttons = [self.button_generators, self.button_auto_clicker, self.button_clickometer]
        for tab_button in self.tab_buttons[1:]:
            tab_button.enabled = False
        
        # setup upgrades
        self.refresh_upgrade_order()
        self.repeating_panel_core_upgrades.set_event_handler('x-refresh-upgrade-order', self.refresh_upgrade_order)
        self.repeating_panel_click_upgrades.set_event_handler('x-refresh-upgrade-order', self.refresh_upgrade_order)
        
        # setup generators tab
        self.repeating_panel_generators.items = Generators.values()

        # setup auto clicker tab
        self.button_auto_click_unlock.enabled = False
        
        # setup clickometer tab        

        # final display update at startup
        Tabs[TAB.GENERATORS].activate()
        self.update_display()
    
    def update_display(self):
        self._update_tick_gain()
        
        self.label_core_points.text = f"{dispnum(CG.core_points)} points"
        self.label_click_points.text = f"{dispnum(CG.click_points)} clicks"
        self.label_clickometer_points.text = f"{dispnum(CG.clickometer_points)} bars"
        
        self.label_tick_gain.text = f"{dispnum(CG.tick_gain)} points / tick"
        self.label_tick_time.text = f"tick: {CG.tick_time:0.2f}s"
        self.label_click_gain.text = f"{dispnum(self._click_gain())} points / click"

        self.label_clicks_per_click.text = f"{dispnum(CG.click_point_gain)} clicks / click"
        self.label_clicks_per_tick.text = f"{dispnum(CG.click_point_tick_gain)} clicks / tick"

        self.progress_clickometer.progress = CG.clickometer_progress / float(CG.clickometer_max)
        self.label_clickometer_progress.text = f"{CG.clickometer_progress} / {CG.clickometer_max}"

        self._update_tabs()
        self._update_core_upgrades()
        self._update_generators_tab()
        self._update_click_upgrades_tab()
        self._update_clickometer_tab()
    
    def _update_tabs(self):
        for tab_button in self.tab_buttons:
            tab = Tabs[tab_button.tag.tab]
            if not tab.unlocked:
                tab_button.tooltip = f"unlock at {dispnum(tab.cost)}"
                if tab.check_unlocked():
                    tab_button.text = tab.name                    
                    tab_button.enabled = True
                    tab_button.tooltip = None
    
    def _update_core_upgrades(self):
        for upgrade_panel in self.repeating_panel_core_upgrades.get_components():
            upgrade_panel.visible = upgrade_panel.item.is_visible()
            if upgrade_panel.visible:
                upgrade_panel.update_display()
    
    def _update_generators_tab(self):
        for generator_panel in self.repeating_panel_generators.get_components():
            generator_panel.visible = generator_panel.item.is_visible()
            if generator_panel.visible:
                generator_panel.update_display()

    def _update_click_upgrades_tab(self):
        CG.game.panel_click_labels.visible = CG.click_point_tick_gain > 0
        for click_upgrade_panel in self.repeating_panel_click_upgrades.get_components():
            click_upgrade_panel.visible = click_upgrade_panel.item.is_visible()
            if click_upgrade_panel.visible:
                click_upgrade_panel.update_display()

    def _update_clickometer_tab(self):
        pass
    
    def _update_tick_gain(self):
        CG.tick_gain = 0
        if not self.repeating_panel_generators.items:
            return
        
        for item in self.repeating_panel_generators.items:
            CG.tick_gain += item.apply()

    def _click_gain(self) -> int:
        gain = CG.click_gain
        if CG.click_percent > 0 and CG.tick_gain > 0:
            gain += CG.click_percent * CG.tick_gain
        if CG.click_logx > 0 and CG.click_points > 0:
            gain *= (1 + CG.click_logx * log2(CG.click_points) / 100.0)
        return floor(gain)
    
    def _apply_button_click_effect(self, manual: bool = False):
        if manual:
            click_point_multi = CG.click_point_gain
        else:
            click_point_multi = CG.click_point_tick_gain

        # update core points
        CG.core_points += self._click_gain() * click_point_multi

        # update click points
        if CG.state >= STATE.AUTO_CLICKER:
            CG.click_points += click_point_multi * (1.0 + CG.click_point_percent)
            self.button_auto_click_unlock.enabled = (CG.click_points >= 10)

        # update clickometer progress
        if CG.state >= STATE.CLICKOMETER:
            CG.clickometer_progress += click_point_multi
            if CG.clickometer_progress >= CG.clickometer_max:
                CG.clickometer_points += CG.clickometer_gain
                CG.clickometer_progress -= CG.clickometer_max
                CG.clickometer_max = int(CG.clickometer_max * 1.01)
    
    # Callbacks

    def refresh_upgrade_order(self, **event_args):
        """callback for resorting the upgrade list order"""
        self.repeating_panel_core_upgrades.items = sorted(CoreUpgrades.values(), key=lambda x: x.cost)
        self.repeating_panel_click_upgrades.items = sorted(ClickUpgrades.values(), key=lambda x: x.cost)
        self.update_display()

    def timer_tick(self, **event_args):
        """This method is called Every [interval] seconds. Does not trigger if [interval] is 0."""
        CG.core_points += CG.tick_gain
        self._apply_button_click_effect()
        self.update_display()
    
    def button_tab_click(self, **event_args):
        """callback on tab button clicks"""
        tab = event_args['sender'].tag.tab
        Tabs[tab].activate()
    
    def button_click_click(self, **event_args):
        """callback on click button clicked"""
        self._apply_button_click_effect(True)
        self.update_display()

    def button_auto_click_unlock_click(self, **event_args):
        """callback on auto click unlock"""
        self.outlined_card_auto_clicker_unlock.visible = False
        CG.click_point_tick_gain = 1
        CG.click_points -= 10
        self.update_display()
        
        
