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
    UPGRADE_2X_A = 1
    UPGRADE_2X_B = 2
    UPGRADE_2X_C = 3
    UPGRADE_2X_D = 4
    UPGRADE_2X_E = 5
    UPGRADE_2X_F = 6
    UPGRADE_2X_G = 7
    UPGRADE_2X_H = 8
    CLICK_2X = 9
    CLICK_TP = 10
    TICK_5P = 11
    

class UT:
    GENERATOR_MULTI = 1
    CLICK_MULTI = 2
    CLICK_PERCENT = 3
    TICK_PERCENT = 4


class TAB:
    GENERATORS = 1
    CLICKOMETER = 2


class CG:
    game = None

    core_points = 0
    click_points = 0
    clickometer_points = 0
    
    tick_gain = 0
    tick_time = 2.0

    click_gain = 1
    click_time = 0
    click_percent = 0.0

    clickometer_gain = 1

    update_generators = True
    update_upgrades = True

    if DEBUG:
        core_points = 99999