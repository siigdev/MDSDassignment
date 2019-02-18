from builder.Builder import *
from executor.Executor import *
from model.Machine import *


builder = Builder()
machine = Machine()

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


# Print states
print("List of all added states: ")
for state in machine.getstates():
    print(" # ", state.name)
    for transition in state.transitions:
        print(" #    ", transition.trigger, " --> ", transition.target)

print("Current state is: ", builder.currentState.name, " and the possible transitions are: ")
for transition in builder.currentState.transitions:
    print(" # ", transition.trigger, " -> ", transition.target)

