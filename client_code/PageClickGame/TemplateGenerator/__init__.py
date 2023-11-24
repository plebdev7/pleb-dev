from ._anvil_designer import TemplateGeneratorTemplate
from anvil import *

class TemplateGenerator(TemplateGeneratorTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Any code you write here will run before the form opens.

    def button_buy_click(self, **event_args):
        """This method is called when the button is clicked"""
        pass
