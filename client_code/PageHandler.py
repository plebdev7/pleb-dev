

class Page:
    # Assigned in FormHome
    GamesList = None
    ClickGame = None
    PotionsGame = None

    Pages = []

    @classmethod
    def generate(cls):
        from .PageGamesList import PageGamesList
        from .PageClickGame import PageClickGame
        from .PagePotionsGame import PagePotionsGame
        
        # Create pages and store global reference
        cls.GamesList = PageGamesList()
        cls.ClickGame = PageClickGame()
        cls.PotionsGame = PagePotionsGame()

        cls.Pages = [cls.GamesList, cls.ClickGame, cls.PotionsGame]

        # Run setup for each page
        for page in cls.Pages:
            if hasattr(page, 'setup'):
                page.setup()