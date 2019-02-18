from model.Machine import Machine
from model.State import State
from model.Transition import *


class Builder:

    currentState = []

    def __init__(self):
        self.machine = Machine()

    def state(self, name):
        self.currentState = State(name)
        self.machine.states.append(self.currentState)
        print("Added the state: ", name)
        return self

    def transition(self, trigger, target):
        self.currentState.transitions.append(Transition(trigger, target));
        print(" -   With a Trigger: ", trigger, " and Target: ", target)
        return self

    def getstates(self):
        return self.machine.states
