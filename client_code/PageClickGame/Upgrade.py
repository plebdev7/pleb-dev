class U:
    UPGRADE_A = 1
    UPGRADE_B = 2
    UPGRADE_C = 3

class Upgrade:
    def __init__(self, name: str, effect: int, cost: int, flag: str):
        self.name = name
        self.effect = effect
        self.cost = cost
        self.flag = flag

Upgrades = [
    Upgrade('upgrade a', '2x generator a', 50, U.UPGRADE_A),
    Upgrade('upgrade b', '2x generator b', 500, U.UPGRADE_B),
    Upgrade('upgrade_c', '2x generator c', 5000, U.UPGRADE_C),
]