from math import ceil

from .ClickGame import CG, C


class ClickUpgrade:
    def __init__(self, name: str, cost: int):
        self.name = name
        self.effect = effect
        self.cost = cost
        self.count = 0
        self.cost_multi = 1.4
        
        self.available = self.cost <= 100

    def is_visible(self) -> bool:
        self.available = self.available or self.cost <= 100 or CG.click_points * 10 >= self.cost
        return self.available
    
    def apply(self) -> int:
        value = self.count * self.effect
        return value

    def current_cost(self) -> int:
        cost = self.cost * self.cost_multi ** self.count
        return ceil(cost)

    def upgrade(self, upgrade_type: int, upgrade_value: float):
        pass

ClickUpgrades = {
    C.CLICK_UPGRADE_AUTO: ClickUpgrade('auto click', 10)
}

Generators = {
    G.GENERATOR_A: Generator('generator a', 1, 10),
    G.GENERATOR_B: Generator('generator b', 5, 100),
    G.GENERATOR_C: Generator('generator c', 20, 1500),
    G.GENERATOR_D: Generator('generator d', 100, 30000),
    G.GENERATOR_E: Generator('generator e', 500, 750000),
    G.GENERATOR_F: Generator('generator f', 2000, 22500000),
    G.GENERATOR_G: Generator('generator g', 10000, 787500000),
    G.GENERATOR_H: Generator('generator h', 50000, 31500000000),
}