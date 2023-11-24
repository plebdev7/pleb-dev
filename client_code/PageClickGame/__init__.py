from ._anvil_designer import PageClickGameTemplate  # type: ignore

# from anvil import *


class PageClickGame(PageClickGameTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        self._score = 0

    def _update_score_label(self):
        self.label_score = self._score

    def button_click_click(self, **event_args):
        """This method is called when the button is clicked"""
        self._score += 1
        self._update_score_label()
