from ._anvil_designer import PageClickGameTemplate  # type: ignore
from .ClickGame import CG
from .Generator import Generators
from .Upgrade import Upgrades

# from anvil import *


class PageClickGame(PageClickGameTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        self.timer.interval = CG.tick
        self.repeating_panel_generators.items = Generators
        self.repeating_panel_upgrades.items = Upgrades

    def update_display(self):
        self._update_gain()
        self.label_score.text = CG.score
        self.label_gain.text = f"{CG.gain} / tick"
        self.label_tick.text = f"tick: {CG.tick}s"
        self.repeating_panel_generators.items = self.repeating_panel_generators.items
    
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
        CG.score += 1
        self._refresh()

    def timer_tick(self, **event_args):
        """This method is called Every [interval] seconds. Does not trigger if [interval] is 0."""
        self._update_score()
        self._refresh()
