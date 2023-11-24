from client_code.Controller import Page
from ._anvil_designer import FormHomeTemplate  # type: ignore

# from anvil import *


class FormHome(FormHomeTemplate):
    def __init__(self, **properties):
        # Create pages
        Page.generate()

        # Attach pages to individual links
        self.link_games.tag.page = Page.GamesList
        self.link_click.tag.page = Page.ClickGame
        self.link_potions.tag.page = Page.PotionsGame

        # set default page as Games List
        self.content_panel.add_component(Page.GamesList)

        # Set Form properties and Data Bindings.
        self.init_components(**properties)

    def nav_link_click(self, **event_args):
        """Generalized click handler for nav links"""
        page = event_args['sender'].tag.page

        self.open_game(page)

    def open_game(self, page):
        # set content to selected page based on nav link click
        self.content_panel.clear()
        self.content_panel.add_component(page)
