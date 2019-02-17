import tkinter

class Executor(object):
    def View(self, x):

        master = tkinter.Tk()

        canvas = tkinter.Canvas(master,height=250, width=300)

        for element in canvas.getelements:
            print("test")
        canvas.pack()
        master.mainloop()
        