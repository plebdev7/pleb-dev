from ._anvil_designer import PageClickGameTemplate  # type: ignore
from .ClickGame import CG
from .Generator import Generator

# from anvil import *


class PageClickGame(PageClickGameTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        self.timer.interval = 2

        self.repeating_panel_generators.items = [
            Generator('generator a', 1, 10),
        ]

    def update_display(self):
        self.label_score.text = CG.Score
        self.repeating_panel_generators.items = self.repeating_panel_generators.items
    
    def _refresh(self):
        self.update_display()

    def _update_score(self):
        for item in self.repeating_panel_generators.items:
            CG.Score += item.apply()

    def button_click_click(self, **event_args):
        """This method is called when the button is clicked"""
        CG.Score += 1
        self._refresh()

    def timer_tick(self, **event_args):
        """This method is called Every [interval] seconds. Does not trigger if [interval] is 0."""
        self._update_score()
        self._refresh()
