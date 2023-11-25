from .Generator import Generator, Generators
from .ClickGame import G, U, UT


class Upgrade:
    def __init__(self, name: str, effect: str, cost: int, upgrade_target: int, upgrade_type: int, upgrade_value: float):
        self.name = name
        self.effect = effect
        self.cost = cost

        self.upgrade_target = upgrade_target
        self.upgrade_type = upgrade_type
        self.upgrade_value = upgrade_value
        
        self.purchased = False

    def apply_upgrade(self) -> None:
        self.purchased = True
        Generators[self.upgrade_target].upgrade(self.upgrade_type, self.upgrade_value)


Upgrades = {
    U.UPGRADE_2X_A: Upgrade('upgrade a', '2x generator a',   50, G.GENERATOR_A, UT.GENERATOR_MULTI, 2.0),
    U.UPGRADE_2X_B: Upgrade('upgrade b', '2x generator b',  500, G.GENERATOR_B, UT.GENERATOR_MULTI, 2.0),
    U.UPGRADE_2X_C: Upgrade('upgrade c', '2x generator c', 5000, G.GENERATOR_C, UT.GENERATOR_MULTI, 2.0),
}