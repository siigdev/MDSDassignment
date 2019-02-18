from builder.Builder import *
from executor.Executor import *


builder = Builder()
machine = Machine()

machine = builder. \
        state("INACTIVE").\
            transition("START", "COOKING").\
        state("COOKING").\
            transition("STOP", "INACTIVE").\
            transition("OPEN", "DOOR_OPEN").\
        state("DOOR_OPEN").\
            transition("CLOSE", "COOKING").\
            transition("STOP", "INACTIVE")



