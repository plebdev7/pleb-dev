DEBUG = True


class G:
    GENERATOR_A = 1
    GENERATOR_B = 2
    GENERATOR_C = 3
    GENERATOR_D = 4
    GENERATOR_E = 5
    GENERATOR_F = 6
    GENERATOR_G = 7
    GENERATOR_H = 8


class U:
    GEN_A_2X = 1
    GEN_B_2X = 2
    GEN_C_2X = 3
    GEN_D_2X = 4
    GEN_E_2X = 5
    GEN_F_2X = 6
    GEN_G_2X = 7
    GEN_H_2X = 8
    CLICK_CORE_2X = 9
    CLICK_BY_TICK = 10
    TICK_5P = 11

    CLICK_CLICK_2X = 1001
    CLICK_TICK_2X = 1002
    CLICK_CORE_LOGX = 1003
    CLICK_SCORE_10P = 1004
    GEN_COST_5P = 1005
    GEN_BONUS_5P = 1006

    CLICKOMETER_SCORE_10P = 2001
    

class UT:
    GENERATOR_MULTI = 1
    CLICK_CORE_MULTI = 2
    CLICK_CORE_PERCENT = 3
    TICK_PERCENT = 4
    
    CLICK_CLICK_MULTI = 1001
    CLICK_TICK_MULTI = 1002
    CLICK_CORE_LOGX = 1003
    CLICK_SCORE_MULTI = 1004
    GEN_COST_PERCENT = 1005
    GEN_BONUS_PERCENT = 1006

    CLICKOMETER_SCORE_MULTI = 2001


class UC:
    SCORE = 1
    CLICKS = 2
    FILLS = 3


class TAB:
    GENERATORS = 1
    AUTO_CLICKER = 2
    CLICKOMETER = 3


class STATE:
    BASE = 1
    AUTO_CLICKER = 2
    CLICKOMETER = 3


class COST:
    AUTO_CLICK = 10
    CLICKOMETER = 1000


class CG:
    game = None
    state = STATE.BASE

    core_points = 0
    click_points = 0
    clickometer_points = 0
    
    tick_gain = 0
    tick_time = 2.0

    click_gain = 1
    click_time = 0
    click_percent = 0.0
    click_logx = 0

    click_point_gain = 1
    click_point_tick_gain = 0
    click_point_percent = 0.0

    clickometer_gain = 0
    clickometer_progress = 0
    clickometer_max = 100

    update_generators = True
    update_upgrades = True

    if DEBUG:
        core_points = 999999
        click_points = 9999