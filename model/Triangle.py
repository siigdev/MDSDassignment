import tkinter

class Triangle(object):
    x = 0,
    y = 0,
    name = ""
    color = "blue"

    def Square(self, name):
        self.name = name

    def setColor(self, color):
        Triangle.color = color
        Triangle.draw(0, 0, 0)

    def draw(self, x, y):
        master = tkinter.Tk()

        canvas = tkinter.Canvas(master,height=250, width=300)
        canvas.create_line(55, 85, 155, 85, 105, 180, 55, 85, fill=Triangle.color)

        canvas.pack()
        master.mainloop()

