from math import ceil

from .Generator import Generator, Generators
from .ClickGame import CG, G, U, UT, UC, STATE
from ..Controller import Page


class Upgrade:
    def __init__(self, name: str, effect: str, cost: int, cost_type: int, upgrade_target: int, upgrade_type: int, upgrade_value: float, upgrade_multi: float):
        self.name = name
        self.effect = effect
        self.cost = cost
        self.cost_type = cost_type

        self.upgrade_target = upgrade_target
        self.upgrade_type = upgrade_type
        self.upgrade_value = upgrade_value
        self.upgrade_multi = upgrade_multi
        
        self.purchased = 0
        self.available = self.cost <= 100

    def get_points(self) -> int:
        points = CG.core_points
        if self.cost_type == UC.CLICKS:
            points = CG.click_points
        elif self.cost_type == UC.FILLS:
            points = CG.clickometer_points

        return points
    
    def is_visible(self) -> bool:
        self.available = self.available or self.cost <= 100 or self.get_points() * 10 >= self.cost
        if self.cost_type == UC.CLICKS and CG.click_point_tick_gain == 0:
            self.available = False
        elif self.cost_type == UC.FILLS and CG.clickometer_gain == 0:
            self.available = False
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
        if upgrade_type == UT.CLICK_CORE_MULTI:
            CG.click_gain = ceil(CG.click_gain * upgrade_value)
        elif upgrade_type == UT.CLICK_CORE_PERCENT:
            CG.click_percent += upgrade_value 
        elif upgrade_type == UT.TICK_PERCENT:
            CG.tick_time = CG.tick_time / (1.0 + upgrade_value)
            Page.ClickGame.timer.interval = CG.tick_time
            
        elif upgrade_type == UT.CLICK_CLICK_MULTI:
            CG.click_point_gain = ceil(CG.click_point_gain * upgrade_value)
        elif upgrade_type == UT.CLICK_TICK_MULTI:
            CG.click_point_tick_gain = ceil(CG.click_point_tick_gain * upgrade_value)
        elif upgrade_type == UT.CLICK_CORE_LOGX:
            CG.click_logx += upgrade_value
        elif upgrade_type == UT.CLICK_SCORE_MULTI:
            CG.click_point_percent += upgrade_value
        elif upgrade_type == UT.GEN_COST_PERCENT:
            for generator in Generators.values():
                generator.cost *= (1.0 + upgrade_value)
        elif upgrade_type == UT.GEN_BONUS_PERCENT:
            for generator in Generators.values():
                generator.effect *= (1.0 + upgrade_value)

        elif upgrade_type == UT.CLICKOMETER_SCORE_MULTI:
            CG.clickometer_gain *= (1.0 + upgrade_value)
        
        Page.ClickGame.update_display()


CoreUpgrades = {
    U.GEN_A_2X: Upgrade('generator a 5x', 'gen a 5x points', Generators[G.GENERATOR_A].cost * 30, UC.SCORE, Generators[G.GENERATOR_A], UT.GENERATOR_MULTI, 5.0, 40),
    U.GEN_B_2X: Upgrade('generator b 5x', 'gen b 5x points', Generators[G.GENERATOR_B].cost * 30, UC.SCORE, Generators[G.GENERATOR_B], UT.GENERATOR_MULTI, 5.0, 40),
    U.GEN_C_2X: Upgrade('generator c 5x', 'gen c 5x points', Generators[G.GENERATOR_C].cost * 30, UC.SCORE, Generators[G.GENERATOR_C], UT.GENERATOR_MULTI, 5.0, 40),
    U.GEN_D_2X: Upgrade('generator d 5x', 'gen d 5x points', Generators[G.GENERATOR_D].cost * 30, UC.SCORE, Generators[G.GENERATOR_D], UT.GENERATOR_MULTI, 5.0, 40),
    U.GEN_E_2X: Upgrade('generator e 5x', 'gen e 5x points', Generators[G.GENERATOR_E].cost * 30, UC.SCORE, Generators[G.GENERATOR_E], UT.GENERATOR_MULTI, 5.0, 40),
    U.GEN_F_2X: Upgrade('generator f 5x', 'gen f 5x points', Generators[G.GENERATOR_F].cost * 30, UC.SCORE, Generators[G.GENERATOR_F], UT.GENERATOR_MULTI, 5.0, 40),
    U.GEN_G_2X: Upgrade('generator g 5x', 'gen g 5x points', Generators[G.GENERATOR_G].cost * 30, UC.SCORE, Generators[G.GENERATOR_G], UT.GENERATOR_MULTI, 5.0, 40),
    U.GEN_H_2X: Upgrade('generator h 5x', 'gen h 5x points', Generators[G.GENERATOR_H].cost * 30, UC.SCORE, Generators[G.GENERATOR_H], UT.GENERATOR_MULTI, 5.0, 40),
    U.CLICK_CORE_2X: Upgrade('5x pts/click', '5x pts/click', 20, UC.SCORE, None, UT.CLICK_CORE_MULTI, 5.0, 20),
    U.CLICK_BY_TICK: Upgrade('+5% gen pts/click', '+5% gen points/click', 1000, UC.SCORE, None, UT.CLICK_CORE_PERCENT, 0.05, 50),
    U.TICK_5P: Upgrade('+10% tick speed', '+10% tick speed', 100, UC.SCORE, None, UT.TICK_PERCENT, 0.1, 10),
}


ClickUpgrades = {
    U.CLICK_CLICK_2X: Upgrade('2x clicks/click', '2x clicks/click', 20, UC.CLICKS, None, UT.CLICK_CLICK_MULTI, 2.0, 10),
    U.CLICK_TICK_2X: Upgrade('2x clicks/tick', '2x clicks/tick', 100, UC.CLICKS, None, UT.CLICK_TICK_MULTI, 2.0, 20),
    # U.CLICK_CORE_LOGX: Upgrade('click val log', '+log(clicks)% pts/click', 500, UC.CLICKS, None, UT.CLICK_CORE_LOGX, 1, 40),
    U.CLICK_SCORE_10P: Upgrade('+10% click pts', '+10% click pts', 30, UC.CLICKS, None, UT.CLICK_SCORE_MULTI, 0.1, 40),
    U.GEN_COST_5P: Upgrade('-10% gen cost', '-10% generator cost', 50, UC.CLICKS, None, UT.GEN_COST_PERCENT, -0.1, 50),
    U.GEN_BONUS_5P: Upgrade('+10% gen pts', '+10% gen points', 250, UC.CLICKS, None, UT.GEN_BONUS_PERCENT, 0.1, 30)
}


ClickometerUpgrades = {
    U.CLICKOMETER_SCORE_10P: Upgrade('+50% fills', '+50% fills', 10, UC.FILLS, None, UT.CLICKOMETER_SCORE_MULTI, 0.5, 10),
}