import tkinter

class Executor():
    def View(self, *args):

        master = tkinter.Tk()

        canvas = tkinter.Canvas(master,height=250, width=300)
        canvas.pack()
        master.mainloop()
        