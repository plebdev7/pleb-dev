from math import floor, ceil

from ._anvil_designer import PageClickGameTemplate  # type: ignore
from .ClickGame import CG, TAB, STATE
from .ClickUpgrade import ClickUpgrades
from .Generator import Generators
from .Tab import Tabs
from .Upgrade import Upgrades

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
        self.repeating_panel_upgrades.set_event_handler('x-refresh-upgrade-order', self.refresh_upgrade_order)
        
        # setup generators tab
        self.repeating_panel_generators.items = Generators.values()

        # setup auto clicker tab
        self.repeating_panel_click_upgrades.items = ClickUpgrades.values()
        
        # setup clickometer tab        

        # final display update at startup
        Tabs[TAB.GENERATORS].activate()
        self.update_display()
    
    def update_display(self):
        self._update_tick_gain()
        
        self.label_core_points.text = CG.core_points
        self.label_click_points.text = f"{CG.click_points} clicks"
        self.label_clickometer_points.text = f"{CG.clickometer_points} bars"
        
        self.label_tick_gain.text = f"{CG.tick_gain} / tick"
        self.label_tick_time.text = f"tick: {CG.tick_time:0.2f}s"

        self.label_click_gain.text = f"{floor(CG.click_gain + CG.click_percent * CG.tick_gain)} / click"

        self.progress_clickometer.progress = CG.clickometer_progress / float(CG.clickometer_max)
        self.label_clickometer_progress.text = f"{CG.clickometer_progress} / {CG.clickometer_max}"

        self._update_tabs()
        self._update_generators_tab()
        self._update_clickometer_tab()

    def _refresh(self):
        self.update_display()
    
    def _update_tabs(self):
        for tab_button in self.tab_buttons:
            tab = Tabs[tab_button.tag.tab]
            if not tab.unlocked:
                tab_button.tooltip = f"unlock at {tab.cost}"
                if tab.check_unlocked():
                    tab_button.text = tab.name                    
                    tab_button.enabled = True
                    tab_button.tooltip = None
    
    def _update_generators_tab(self):
        for generator_panel in self.repeating_panel_generators.get_components():
            generator_panel.visible = generator_panel.item.is_visible()
            if generator_panel.visible:
                generator_panel.update_display()
                
        for upgrade_panel in self.repeating_panel_upgrades.get_components():
            upgrade_panel.visible = upgrade_panel.item.is_visible()
            if upgrade_panel.visible:
                upgrade_panel.update_display()

    def _update_clickometer_tab(self):
        pass
    
    def _update_tick_gain(self):
        CG.tick_gain = 0
        if not self.repeating_panel_generators.items:
            return
        
        for item in self.repeating_panel_generators.items:
            CG.tick_gain += item.apply()
    
    def _update_core_points(self):
        CG.core_points += CG.tick_gain

    # Callbacks

    def refresh_upgrade_order(self, **event_args):
        self.repeating_panel_upgrades.items = sorted(Upgrades.values(), key=lambda x: x.cost)
        self.update_display()
    
    def button_click_click(self, **event_args):
        """This method is called when the button is clicked"""
        CG.core_points += floor(CG.click_gain + CG.click_percent * CG.tick_gain)
        if CG.state >= STATE.AUTO_CLICKER:
            CG.click_points += 1
        if CG.state >= STATE.CLICKOMETER:
            CG.clickometer_progress += 1
            if CG.clickometer_progress >= CG.clickometer_max:
                CG.clickometer_points += 1
                CG.clickometer_progress -= CG.clickometer_max
                CG.clickometer_max = int(CG.clickometer_max * 1.01)
        self._refresh()

    def timer_tick(self, **event_args):
        """This method is called Every [interval] seconds. Does not trigger if [interval] is 0."""
        self._update_core_points()
        self._refresh()

    def button_tab_click(self, **event_args):
        tab = event_args['sender'].tag.tab
        Tabs[tab].activate()
        
