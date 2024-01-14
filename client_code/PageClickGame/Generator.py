from math import ceil

from .ClickGame import CG, G, UT


class Generator:
    def __init__(self, name: str, effect: int, cost: int):
        self.name = name
        self.effect = effect
        self.cost = cost
        self.count = 0
        self.cost_multi = 1.4
        
        self.available = self.cost <= 100

    def is_visible(self) -> bool:
        self.available = self.available or self.cost <= 100 or CG.core_points * 10 >= self.cost
        return self.available
    
    def apply(self) -> int:
        value = self.count * self.effect
        return value

    def current_cost(self) -> int:
        cost = self.cost * self.cost_multi ** self.count
        return ceil(cost)

    def upgrade(self, upgrade_type: int, upgrade_value: float):
        if upgrade_type == UT.GENERATOR_MULTI:
            self.effect = ceil(self.effect * upgrade_value)


Generators = {
    G.GENERATOR_A: Generator('generator a', 5**0, 10),
    G.GENERATOR_B: Generator('generator b', 5**1, 100),
    G.GENERATOR_C: Generator('generator c', 5**2, 1500),
    G.GENERATOR_D: Generator('generator d', 5**3, 30000),
    G.GENERATOR_E: Generator('generator e', 5**4, 750000),
    G.GENERATOR_F: Generator('generator f', 5**5, 22500000),
    G.GENERATOR_G: Generator('generator g', 5**6, 787500000),
    G.GENERATOR_H: Generator('generator h', 5**7, 31500000000),
}