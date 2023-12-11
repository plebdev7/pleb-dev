from math import ceil

from .Generator import Generator, Generators
from .ClickGame import CG, G, U, UT
from ..Controller import Page


class Upgrade:
    def __init__(self, name: str, effect: str, cost: int, upgrade_target: int, upgrade_type: int, upgrade_value: float, upgrade_multi: float):
        self.name = name
        self.effect = effect
        self.cost = cost

        self.upgrade_target = upgrade_target
        self.upgrade_type = upgrade_type
        self.upgrade_value = upgrade_value
        self.upgrade_multi = upgrade_multi
        
        self.purchased = 0
        self.available = self.cost <= 100

    def is_visible(self) -> bool:
        self.available = self.available or self.cost <= 100 or CG.core_points * 10 >= self.cost
        return self.available
    
    def apply_upgrade(self) -> None:
        self.available = False
        self.purchased += 1
        self.cost = ceil(self.cost * self.upgrade_multi)
        target = self
        if self.upgrade_target:
            target = self.upgrade_target
        target.upgrade(self.upgrade_type, self.upgrade_value)

    def upgrade(self, upgrade_type: int, upgrade_value: float):
        if upgrade_type == UT.CLICK_MULTI:
            CG.click_gain = ceil(CG.click_gain * upgrade_value)
        elif upgrade_type == UT.CLICK_PERCENT:
            CG.click_percent += upgrade_value 
        elif upgrade_type == UT.TICK_PERCENT:
            CG.tick_time = CG.tick_time / (1.0 + upgrade_value)
            Page.ClickGame.timer.interval = CG.tick_time
        Page.ClickGame.update_display()


CoreUpgrades = {
    U.UPGRADE_2X_A: Upgrade('upgrade a', '2x generator a', Generators[G.GENERATOR_A].cost * 5, Generators[G.GENERATOR_A], UT.GENERATOR_MULTI, 2.0, 17),
    U.UPGRADE_2X_B: Upgrade('upgrade b', '2x generator b', Generators[G.GENERATOR_B].cost * 6, Generators[G.GENERATOR_B], UT.GENERATOR_MULTI, 2.0, 18),
    U.UPGRADE_2X_C: Upgrade('upgrade c', '2x generator c', Generators[G.GENERATOR_C].cost * 7, Generators[G.GENERATOR_C], UT.GENERATOR_MULTI, 2.0, 19),
    U.UPGRADE_2X_D: Upgrade('upgrade d', '2x generator d', Generators[G.GENERATOR_D].cost * 8, Generators[G.GENERATOR_D], UT.GENERATOR_MULTI, 2.0, 20),
    U.UPGRADE_2X_E: Upgrade('upgrade e', '2x generator e', Generators[G.GENERATOR_E].cost * 9, Generators[G.GENERATOR_E], UT.GENERATOR_MULTI, 2.0, 21),
    U.UPGRADE_2X_F: Upgrade('upgrade f', '2x generator f', Generators[G.GENERATOR_F].cost * 10, Generators[G.GENERATOR_F], UT.GENERATOR_MULTI, 2.0, 22),
    U.UPGRADE_2X_G: Upgrade('upgrade g', '2x generator g', Generators[G.GENERATOR_G].cost * 11, Generators[G.GENERATOR_G], UT.GENERATOR_MULTI, 2.0, 23),
    U.UPGRADE_2X_H: Upgrade('upgrade h', '2x generator h', Generators[G.GENERATOR_H].cost * 12, Generators[G.GENERATOR_H], UT.GENERATOR_MULTI, 2.0, 24),
    U.CLICK_2X: Upgrade('upgrade click', '2x click value', 20, None, UT.CLICK_MULTI, 2.0, 3.3),
    U.CLICK_TP: Upgrade('click by tick', 'click value +1% tick', 1000, None, UT.CLICK_PERCENT, 0.01, 15),
    U.TICK_5P: Upgrade('upgrade tick', '+5% tick speed', 100, None, UT.TICK_PERCENT, 0.05, 6.7),
}