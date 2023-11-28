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
            
            


Tabs = {
    TAB.GENERATORS: Tab('generators', 0),
    TAB.CLICKOMETER: Tab('clickometer', 100000),
}