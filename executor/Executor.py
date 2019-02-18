from model.State import *
from model.Transition import *
from builder.Builder import *
from model.Machine import *


class Executor:
    def __init__(self, machine):
        self.machine = machine
        self.currentState = State("START")

    def test(self, trigger):
        for state in self.machine.states:
            if state.name == self.currentState.name:
                for transition in state.transitions:
                    if transition.trigger == trigger:
                        print("WE ARE HERE")
                print("WE ARE NOT HERE")
        print("NOT AT ALL")
