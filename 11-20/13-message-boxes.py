from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Tk Examples")

# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno

def popup():
    response = messagebox.askyesno("This is my popup !", "Hello World !")

    if response == 1:
        Label(root, text="You clicked YES !").pack()
    else:
        Label(root, text="You clicked NO !").pack()

Button(root, text="Popup", command=popup).pack()

root.mainloop()