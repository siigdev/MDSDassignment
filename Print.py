from model.Metamodel import *

# Printing the State Machine
print("List of all added states: ")
for state in machine.getstates():
    print(" # ", state.name)
    for transition in state.transitions:
        print(" #    ", transition.trigger, " --> ", transition.target)

# Printing the current State and possible Transitions
print("Current state is: ", builder.currentState.name, " and the possible transitions are: ")
for transition in builder.currentState.transitions:
    print(" # ", transition.trigger, " -> ", transition.target)
