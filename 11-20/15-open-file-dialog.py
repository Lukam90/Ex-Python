from tkinter import *
from tkinter import filedialog

from PIL import Image, ImageTk

root = Tk()
root.title("Tk Examples")

def open():
    global my_image

    root.filename = filedialog.askopenfilename(initialdir="./images", title="Select a file", filetypes=(("png files", "*.png"), ("jpg files", "*.jpg"), ("all files", "*.*")))

    Label(root, text=root.filename).pack()
    
    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    
    Label(image=my_image).pack()

my_btn = Button(root, text="Open File", command=open).pack()

root.mainloop()