from ._anvil_designer import FormHomeTemplate
from anvil import *

from ..PageHandler import Page
from ..PageGamesList import PageGamesList
from ..PageClickGame import PageClickGame
from ..PagePotionsGame import PagePotionsGame

class FormHome(FormHomeTemplate):
    def __init__(self, **properties):
        # Create pages and store global reference
        Page.GamesList = PageGamesList()
        Page.ClickGame = PageClickGame()
        Page.PotionsGame = PagePotionsGame()

        # Run setup for each page
        for page in Page.Pages:
            if hasattr(page, 'setup'):
                page.setup()
        
        # Attach pages to individual links
        self.link_games.tag.form_to_open = Page.GamesList
        self.link_click.tag.form_to_open = Page.ClickGame
        self.link_potions.tag.form_to_open = Page.PotionsGame

        # set default page as Games List
        self.content_panel.add_component(Page.GamesList)
        
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

    def nav_link_click(self, **event_args):
        """Generalized click handler for nav links"""
        form_to_open = event_args['sender'].tag.form_to_open
        self.open_game(form_to_open)

    def open_game(self, form_to_open):
        # set content to selected page based on nav link click
        self.content_panel.clear()
        self.content_panel.add_component(form_to_open)