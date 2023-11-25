from ._anvil_designer import TemplateUpgradeTemplate
from anvil import *

from ..ClickGame import CG
from ...Controller import Page

class TemplateUpgrade(TemplateUpgradeTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)
        self.update_display()

    def update_display(self):
        self.label_name.text = f"{self.item.name}"
        self.label_effect.text = f"{self.item.effect}"
        self.button_buy.text = f"cost: {self.item.cost}"
        self.button_buy.enabled = CG.score >= self.item.cost

    def button_buy_click(self, **event_args):
        """This method is called when the button is clicked"""
        pass
