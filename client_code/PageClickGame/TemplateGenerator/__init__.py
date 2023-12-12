from ._anvil_designer import TemplateGeneratorTemplate
from anvil import *

from ..ClickGame import CG

class TemplateGenerator(TemplateGeneratorTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties) 
        self.update_display()

    def update_display(self):
        cost = self.item.current_cost()
        self.label_name.text = f"{self.item.name} ({self.item.count})"    
        self.label_effect.text = f"{self.item.effect} points / tick"
        self.button_buy.text = f"{cost} points"
        
        self.button_buy.enabled = CG.core_points >= cost
    
    def button_buy_click(self, **event_args):
        """This method is called when the button is clicked"""
        self.button_buy.enabled = False
        CG.core_points -= self.item.current_cost()
        self.item.count += 1
        
        self.update_display()
        CG.game.update_display()
