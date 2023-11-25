DEBUG = False


class G:
    GENERATOR_A = 1
    GENERATOR_B = 2
    GENERATOR_C = 3


class U:
    UPGRADE_2X_A = 1
    UPGRADE_2X_B = 2
    UPGRADE_2X_C = 3
    CLICK_2X = 4
    TICK_5P = 5


class UT:
    GENERATOR_MULTI = 1
    CLICK_MULTI = 2
    TICK_PERCENT = 3


class CG:
    score = 0
    gain = 0
    click = 1
    tick = 2.0

    if DEBUG:
        score = 100