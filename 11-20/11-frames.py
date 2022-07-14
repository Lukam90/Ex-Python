from tkinter import *

root = Tk()
root.title("Tk Examples")

frame = LabelFrame(root, text="This is my frame...", padx=5, pady=5)
frame.pack(padx=10, pady=10)

btn1 = Button(frame, text="Don't click here !")
btn2 = Button(frame, text="...or here !")

btn1.grid(row=0, column=0)
btn2.grid(row=1, column=1)

root.mainloop()