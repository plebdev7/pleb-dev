from math import floor, ceil

from ._anvil_designer import PageClickGameTemplate  # type: ignore
from .ClickGame import CG
from .Generator import Generators
from .Upgrade import Upgrades, UT

# from anvil import *


class PageClickGame(PageClickGameTemplate):
    TITLE = 'click'
    
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        self.timer.interval = CG.tick
        self.repeating_panel_generators.items = Generators.values()
        self.refresh_upgrade_order()

        self.repeating_panel_upgrades.set_event_handler('x-refresh-upgrade-order', self.refresh_upgrade_order)
        
    def update_display(self):
        self._update_gain()
        self.label_score.text = CG.score
        self.label_click.text = f"{floor(CG.click + CG.click_percent * CG.gain)} / click"
        self.label_gain.text = f"{CG.gain} / tick"
        self.label_tick.text = f"tick: {CG.tick:0.2f}s"

        for generator_panel in self.repeating_panel_generators.get_components():
            generator_panel.visible = generator_panel.item.is_visible()
            if generator_panel.visible:
                generator_panel.update_display()
                
        for upgrade_panel in self.repeating_panel_upgrades.get_components():
            upgrade_panel.visible = upgrade_panel.item.is_visible()
            if upgrade_panel.visible:
                upgrade_panel.update_display()

    def upgrade(self, upgrade_type: int, upgrade_value: float):
        if upgrade_type == UT.CLICK_MULTI:
            CG.click = ceil(CG.click * upgrade_value)
        elif upgrade_type == UT.CLICK_PERCENT:
            CG.click_percent += upgrade_value 
        elif upgrade_type == UT.TICK_PERCENT:
            CG.tick = CG.tick / (1.0 + upgrade_value)
            self.timer.interval = CG.tick
        self.update_display()
    
    def _refresh(self):
        self.update_display()

    def _update_gain(self):
        CG.gain = 0
        if not self.repeating_panel_generators.items:
            return
        
        for item in self.repeating_panel_generators.items:
            CG.gain += item.apply()
    
    def _update_score(self):
        CG.score += CG.gain

    def refresh_upgrade_order(self, **event_args):
        self.repeating_panel_upgrades.items = sorted(Upgrades.values(), key=lambda x: x.cost)
        self.update_display()
    
    def button_click_click(self, **event_args):
        """This method is called when the button is clicked"""
        CG.score += floor(CG.click + CG.click_percent * CG.gain)
        self._refresh()

    def timer_tick(self, **event_args):
        """This method is called Every [interval] seconds. Does not trigger if [interval] is 0."""
        self._update_score()
        self._refresh()
