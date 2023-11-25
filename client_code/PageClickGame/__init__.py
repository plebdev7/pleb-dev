from math import ceil

from ._anvil_designer import PageClickGameTemplate  # type: ignore
from .ClickGame import CG
from .Generator import Generators
from .Upgrade import Upgrades, UT

# from anvil import *


class PageClickGame(PageClickGameTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        self.timer.interval = CG.tick
        self.repeating_panel_generators.items = Generators.values()
        self.repeating_panel_upgrades.items = sorted(Upgrades.values(), key=lambda x: x.cost)
        self.update_display()

    def update_display(self):
        self._update_gain()
        self.label_score.text = CG.score
        self.label_click.text = f"{CG.click} / click"
        self.label_gain.text = f"{CG.gain} / tick"
        self.label_tick.text = f"tick: {CG.tick:0.2f}s"
        self.repeating_panel_generators.items = self.repeating_panel_generators.items
        self.repeating_panel_upgrades.items = [item for item in self.repeating_panel_upgrades.items if not item.purchased]

    def upgrade(self, upgrade_type: int, upgrade_value: float):
        if upgrade_type == UT.CLICK_MULTI:
            CG.click = ceil(CG.click * upgrade_value)
        elif upgrade_type == UT.TICK_PERCENT:
            CG.tick = CG.tick / (1.0 + upgrade_value)
            self.timer.interval = CG.tick
        self.update_display()
    
    def _refresh(self):
        self.update_display()

    def _update_gain(self):
        CG.gain = 0
        for item in self.repeating_panel_generators.items:
            CG.gain += item.apply()
    
    def _update_score(self):
        CG.score += CG.gain

    def button_click_click(self, **event_args):
        """This method is called when the button is clicked"""
        CG.score += CG.click
        self._refresh()

    def timer_tick(self, **event_args):
        """This method is called Every [interval] seconds. Does not trigger if [interval] is 0."""
        self._update_score()
        self._refresh()
