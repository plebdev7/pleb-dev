from ._anvil_designer import PageGamesListTemplate
from anvil import *

from ..PageHandler import Page

class PageGamesList(PageGamesListTemplate):
    def __init__(self, **properties):             
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

    def setup(self):
        """Call during form init"""
        
        # Attach pages to individual links
        self.button_click.tag.form_to_open = Page.ClickGame
        self.button_potions.tag.form_to_open = Page.PotionsGame

        print(Page.ClickGame)

    def game_link_click(self, **event_args):
        """Generalized click handler for game links"""
        form_to_open = event_args['sender'].tag.form_to_open
        get_open_form().open_game(form_to_open)
        