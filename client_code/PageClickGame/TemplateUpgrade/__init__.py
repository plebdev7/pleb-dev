from ._anvil_designer import TemplateUpgradeTemplate
from anvil import *

from ..ClickGame import CG

class TemplateUpgrade(TemplateUpgradeTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)
        self.update_display()

    def update_display(self):
        self.label_name.text = f"{self.item.name}"
        self.button_buy.text = f"cost: {self.item.cost}"
        

        tooltip = f"{self.item.effect}"
        self.tooltip = tooltip
        self.label_name.tooltip = tooltip
        self.button_buy.tooltip = tooltip

        self.button_buy.enabled = CG.score >= self.item.cost

    def button_buy_click(self, **event_args):
        """This method is called when the button is clicked"""
        self.button_buy.enabled = False
        CG.score -= self.item.cost
        self.item.apply_upgrade()        
        CG.game.update_display()

        self.parent.raise_event('x-refresh-upgrade-order')