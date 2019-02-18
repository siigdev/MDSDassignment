from model.State import *
from model.Transition import *
from builder.Builder import *
from model.Machine import *


class Executor:
    def __init__(self, machine):
        self.machine = machine
        self.currentState = State("START")