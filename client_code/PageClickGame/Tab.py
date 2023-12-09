from .ClickGame import CG, TAB, STATE
from .State import activate_state


class Tab:
    def __init__(self, name, cost, unlock_state = None):
        self.name = name
        self.cost = cost
        self.unlocked = False
        self.unlock_state = unlock_state

    def check_unlocked(self):
        if CG.core_points >= self.cost and not self.unlocked:
            self.unlocked = True
            activate_state(self.unlock_state)
                
        return self.unlocked

    def activate(self):
        tab_button = getattr(CG.game, f'button_{self.name}')
        tab_card = getattr(CG.game, f'outlined_card_{self.name}')

        tab_button.role = 'filled-button'
        tab_card.visible = True

        # deactivate all other tabs
        for tab in Tabs.values():
            if tab != self:
                tab.deactivate()
        
    def deactivate(self):
        tab_button = getattr(CG.game, f'button_{self.name}')
        tab_card = getattr(CG.game, f'outlined_card_{self.name}')

        tab_button.role = 'tonal-button'
        tab_card.visible = False
            

Tabs = {
    TAB.GENERATORS: Tab('generators', 0),
    TAB.AUTO_CLICKER: Tab('auto_clicker', 10000, STATE.AUTO_CLICKER),
    TAB.CLICKOMETER: Tab('clickometer', 1000000, STATE.CLICKOMETER),
}