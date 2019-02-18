from executor.Executor import *
from model.Machine import *


builder = Builder()

# Microwave Oven Metamodel 
machine = builder. \
        state("INACTIVE").\
            transition("START", "COOKING").\
        state("COOKING").\
            transition("STOP", "INACTIVE").\
            transition("OPEN", "DOOR_OPEN").\
        state("DOOR_OPEN").\
            transition("CLOSE", "COOKING").\
            transition("STOP", "INACTIVE")



