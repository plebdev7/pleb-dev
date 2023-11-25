from .Generator import Generator, Generators
from .ClickGame import CG, G, U, UT
from ..Controller import Page


class Upgrade:
    def __init__(self, name: str, effect: str, cost: int, upgrade_target: int, upgrade_type: int, upgrade_value: float):
        self.name = name
        self.effect = effect
        self.cost = cost

        self.upgrade_target = upgrade_target
        self.upgrade_type = upgrade_type
        self.upgrade_value = upgrade_value
        
        self.purchased = False
        self.available = self.cost <= 100

    def is_visible(self) -> bool:
        self.available = self.cost <= 100 or CG.score * 10 >= self.cost
        return self.available and not self.purchased
    
    def apply_upgrade(self) -> None:
        self.purchased = True
        if not self.upgrade_target:
            self.upgrade_target = Page.ClickGame
        self.upgrade_target.upgrade(self.upgrade_type, self.upgrade_value)


Upgrades = {
    U.UPGRADE_2X_A: Upgrade('upgrade a', '2x generator a', 50, Generators[G.GENERATOR_A], UT.GENERATOR_MULTI, 2.0),
    U.UPGRADE_2X_B: Upgrade('upgrade b', '2x generator b', 500, Generators[G.GENERATOR_B], UT.GENERATOR_MULTI, 2.0),
    U.UPGRADE_2X_C: Upgrade('upgrade c', '2x generator c', 5000, Generators[G.GENERATOR_C], UT.GENERATOR_MULTI, 2.0),
    U.CLICK_2X: Upgrade('upgrade click', '2x click value', 20, None, UT.CLICK_MULTI, 2.0),
    U.TICK_5P: Upgrade('upgrade tick', '+5% tick speed', 100, None, UT.TICK_PERCENT, 0.05),
}