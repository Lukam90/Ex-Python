from tkinter import *

root = Tk()
root.title("Tk Examples")

def open():
    top = Toplevel()
    top.title("My second window")

    Label(top, text="Hello World !").pack()

btn = Button(root, text="Open Second Window", command=open).pack()

root.mainloop()