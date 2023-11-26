from ._anvil_designer import TemplateGeneratorTemplate
from anvil import *

from ..ClickGame import CG
from ...Controller import Page

class TemplateGenerator(TemplateGeneratorTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)        
        self.update_display()

    def update_display(self):
        cost = self.item.current_cost()
        self.label_name.text = f"{self.item.name} ({self.item.count})"        
        self.button_buy.text = f"cost: {cost}"

        tooltip = f"{self.item.effect}/tick"
        self.tooltip = tooltip
        self.label_name.tooltip = tooltip
        self.button_buy.tooltip = tooltip
        
        self.button_buy.enabled = CG.score >= cost
    
    def button_buy_click(self, **event_args):
        """This method is called when the button is clicked"""
        CG.score -= self.item.current_cost()
        self.item.count += 1
        
        self.update_display()
        Page.ClickGame.update_display()
