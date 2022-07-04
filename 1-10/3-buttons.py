from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root, text="Look ! I clicked a button !")
    myLabel.pack()

myButton = Button(root, text="Click Me !", pady=50, command=myClick)
myButton.pack()

root.mainloop()