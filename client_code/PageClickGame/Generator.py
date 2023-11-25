class Generator:
    def __init__(self, name: str, effect: int, cost: int):
        self.name = name
        self.effect = effect
        self.cost = cost
        self.count = 0

    def apply(self) -> int:
        value = self.count * self.effect
        return value       