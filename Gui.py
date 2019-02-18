import tkinter
from model.Metamodel import *

class Gui:
    def __init__(self):
        window = tkinter.Tk()
        window.title("Microwave State Machine")
        window.geometry('200x150')

        currstatelbl = tkinter.Label(window, text="Current state: ")
        currstatelbl.grid(column=0, row=0)
        self.currstate = tkinter.Label(window, text=builder.currentState.name)
        self.currstate.grid(column=1, row=0)
        start = tkinter.Button(window, text="Start", command=self.start)
        start.grid(column=0, row=1)
        stop = tkinter.Button(window, text="Stop", command=self.stop)
        stop.grid(column=0, row=2)
        open = tkinter.Button(window, text="Open", command=self.open)
        open.grid(column=0, row=3)
        close = tkinter.Button(window, text="Close", command=self.close)
        close.grid(column=0, row=4)
        window.mainloop()

    def start(self):
        self.check("START")

    def stop(self):
        self.check("STOP")

    def open(self):
        self.check("OPEN")

    def close(self):
        self.check("CLOSE")

    def check(self, trigger):
        for state in machine.getstates():
            if state.name == builder.currentState.name:
                for transition in state.transitions:
                    if transition.trigger == trigger:
                        builder.currentState = State(transition.target)
                        self.currstate.configure(text=builder.currentState.name)


if __name__ == "__main__":
    Gui()