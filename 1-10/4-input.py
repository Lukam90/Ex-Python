from tkinter import *

root = Tk()

entry = Entry(root, width=50)
entry.pack()

def myClick():
    myLabel = Label(root, text="Hello " + entry.get())
    myLabel.pack()

myButton = Button(root, text="Enter Your Name", command=myClick)
myButton.pack()

root.mainloop()