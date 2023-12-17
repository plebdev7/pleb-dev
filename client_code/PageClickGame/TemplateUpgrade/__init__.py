from ._anvil_designer import TemplateUpgradeTemplate
from anvil import *

from ..ClickGame import CG, UC
from ...Utilities import dispnum

class TemplateUpgrade(TemplateUpgradeTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)
        self.update_display()

    def update_display(self):
        cost_type = 'points'
        if self.item.cost_type == UC.CLICKS:
            cost_type = 'clicks'
        elif self.item.cost_type == UC.FILLS:
            cost_type = 'fills'
        
        self.label_name.text = f"{self.item.name}"
        self.label_effect.text = f"{self.item.effect}"
        self.button_buy.text = f"{dispnum(self.item.cost)} {cost_type}"

        self.button_buy.enabled = self.item.get_points() >= self.item.cost

    def button_buy_click(self, **event_args):
        """This method is called when the button is clicked"""
        self.button_buy.enabled = False
        if self.item.cost_type == UC.SCORE:
            CG.core_points -= self.item.cost
        elif self.item.cost_type == UC.CLICKS:
            CG.click_points -= self.item.cost
        elif self.item.cost_type == UC.FILLS:
            CG.clickometer_points -= self.item.cost
        self.item.apply_upgrade()        
        CG.game.update_display()

        self.parent.raise_event('x-refresh-upgrade-order')
