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
        print("added ", name)
        return self

    def transition(self, trigger, target):
        self.currentState.transitions.append(Transition(trigger, target));
        print("Transition to: ", self.currentState.name, " with trigger: ", trigger, " and target: ", target)
        return self

    def getmachine(self):
        return self.machine
