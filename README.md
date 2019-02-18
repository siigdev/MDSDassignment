## Model-Driven Software Development Project Assignment 1
This features an internal domain specific language for defining state machines. The DSL is written in Python and includes a working metamodel of a microwave oven with an additional graphical user interface for convinience.
The GUI is not yet fully functional yet, but provides some initial functionality. The program can also be run through Metamodel.py which prints out the states and transitions.

### Syntax

```
builder.
  state("NAME_OF_STATE").
    transition("TRANSITION_TRIGGER", "TRANSITION_TARGET")
```

### Requirements
- Python 3+
- PyQt
