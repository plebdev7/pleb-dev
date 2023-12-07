from .ClickGame import CG, TAB


class Tab:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost
        self.unlocked = False

    def check_unlocked(self):
        if CG.score >= self.cost:
            self.unlocked = True
        return self.unlocked

    def activate(self):
        tab_button = getattr(CG.game, f'button_{self.name}')
        tab_card = getattr(CG.game, f'card_{self.name}')

        tab_button.role = 'filled-button'
        tab_card.visible = True

        # deactivate all other tabs
        for tab in Tabs.values():
            if tab != self:
                tab.deactivate()
        
    def deactivate(self):
        tab_button = getattr(CG.game, f'button_{self.name}')
        tab_card = getattr(CG.game, f'card_{self.name}')

        tab_button.role = 'tonal-button'
        tab_card.visible = False
            
            


Tabs = {
    TAB.GENERATORS: Tab('generators', 0),
    TAB.CLICKOMETER: Tab('clickometer', 100000),
}