from client_code.Controller import Page
from ._anvil_designer import PageGamesListTemplate  # type: ignore
from anvil import get_open_form


from ..PageHandler import Page

class PageGamesList(PageGamesListTemplate):
    def __init__(self, **properties):             
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

    def setup(self):
        """Call during form init"""

        # Attach pages to individual links
        self.button_click.tag.page = Page.ClickGame
        self.button_potions.tag.page = Page.PotionsGame

        print(self.button_click.tag)

        print(Page.ClickGame)

    def game_link_click(self, **event_args):
        """Generalized click handler for game links"""
        print(self.button_click.tag)

        page = event_args['sender'].tag.page
        get_open_form().open_game(page)

