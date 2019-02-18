import tkinter
from RunTest import *
from executor.Executor import *

executor = Executor(builder.getmachine())
print(builder.currentState.name)
executor.test("START")
executor.test("CLOSE")

class Gui:
    def __init__(self):
        self.currentState = "INACTIVE"
        window = tkinter.Tk()
        window.title("Microwave State Machine")
        window.geometry('200x150')
        currstatelbl = tkinter.Label(window, text="Current state: ")
        currstatelbl.grid(column=0, row=0)
        self.currstate = tkinter.Label(window, text="?")
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
        self.currstate.configure(text="reset")
        for transition in builder.currentState.transitions:
            print("DE ER HER: ", transition.trigger, " -> ", transition.target)
            if transition.trigger == "START":
                self.currstate.configure(text=transition.target)
                builder.currentState = State(transition.target)
                print(builder.currentState.name)
            else:
                self.currstate.configure(text="You can only use: " + transition.trigger)

    def stop(self):
        for transition in builder.currentState.transitions:
            print("DE ER HER: ", transition.trigger, " -> ", transition.target)
            if transition.trigger == "STOP":
                self.currstate.configure(text=transition.target)
                builder.currentState = State(transition.target)
                print(builder.currentState.name)

    def open(self):
        for transition in builder.currentState.transitions:
            print("DE ER HER: ", transition.trigger, " -> ", transition.target)
            if transition.trigger == "OPEN":
                self.currstate.configure(text=transition.target)
                builder.currentState = State(transition.target)
                print(builder.currentState.name)

    def close(self):
        for transition in builder.currentState.transitions:
            print("DE ER HER: ", transition.trigger, " -> ", transition.target)
            if transition.trigger == "CLOSE":
                self.currstate.configure(text=transition.target)
                builder.currentState = State(transition.target)
                print(builder.currentState.name)

Gui()