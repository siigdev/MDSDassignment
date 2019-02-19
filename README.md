## Model-Driven Software Development Assignment 1
This features an internal domain specific language for defining state machines. The DSL is written in Python and includes a working metamodel of a microwave oven with an additional graphical user interface for convinience located in **Gui.py**. The program can also be run through **Print.py** which prints out the initialized states and transitions.

DSL Syntax
-----

```
builder.
  state("NAME_OF_STATE").
    transition("TRANSITION_TRIGGER", "TRANSITION_TARGET")
```

Requirements
-----
- Python3
- Tkinter (Optional)
