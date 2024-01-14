from .ClickGame import CG, STATE

class State:    
    def enter(self):
        pass

    def exit(self):
        pass


class StateAutoClicker(State):
    def enter(self):
        pass

class StateClickometer(State):
    def enter(self):
        pass


States = {
    STATE.AUTO_CLICKER: StateAutoClicker(),
    STATE.CLICKOMETER: StateClickometer(),
}


def activate_state(new_state):
    if new_state not in States:
        return

    prev_state = CG.state
    if prev_state in States:
        States[prev_state].exit()
    States[new_state].enter()
    CG.state = new_state