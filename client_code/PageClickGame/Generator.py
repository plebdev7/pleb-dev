from math import ceil

class Generator:
    def __init__(self, name: str, effect: int, cost: int):
        self.name = name
        self.effect = effect
        self.cost = cost
        self.count = 0
        self.cost_multi = 1.4

    def apply(self) -> int:
        value = self.count * self.effect
        return value

    def current_cost(self) -> int:
        cost = self.cost * self.cost_multi ** self.count
        return ceil(cost)