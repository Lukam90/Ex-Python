from tkinter import *

root = Tk()
root.title("Tk Examples")

TOPPINGS = [
    ("Pepperoni", "Pepperoni"),
    ("Cheese", "Cheese"),
    ("Mushroom", "Mushroom"),
    ("Onion", "Onion")
]

pizza = StringVar()
pizza.set("Pepperoni")

for text, tapping in TOPPINGS:
    Radiobutton(root, text=text, variable=pizza, value=tapping).pack(anchor=W)

def clicked(value):
    myLabel = Label(root, text=value)
    myLabel.pack()

myButton = Button(root, text="Click Me !", command=lambda: clicked(pizza.get()))
myButton.pack()

root.mainloop()