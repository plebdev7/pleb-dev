from ._anvil_designer import FormHomeTemplate
from anvil import *

from ..PageGamesList import PageGamesList
from ..PagePotionsGame import PagePotionsGame

class FormHome(FormHomeTemplate):
    def __init__(self, **properties):
        # Create references to all pages
        self.page_games_list = PageGamesList()
        self.page_potions = PagePotionsGame()

        # Attach pages to individual links
        self.link_games.tag.form_to_open = self.page_games_list
        self.link_potions.tag.form_to_open = self.page_potions

        # set default page as Games List
        self.content_panel.add_component(self.page_games_list)
        
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

    def nav_link_click(self, **event_args):
        """Generalized click handler for nav links"""
        form_to_open = event_args['sender'].tag.form_to_open

        # set content to selected page based on nav link click
        self.content_panel.clear()
        self.content_panel.add_component(form_to_open)

    