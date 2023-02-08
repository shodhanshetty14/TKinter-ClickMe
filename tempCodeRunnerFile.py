from tkinter import *
from tkinter import ttk
from random import randint

root = Tk()
root.title("Click me If you can")
root.geometry("500x500")
content = ttk.Frame(root)
def randomLocation():
    new_x = randint(10, 500)
    new_y = randint(10,500)
    button.place_configure(x=new_x, y= new_y)


label1 = ttk.Label(root, text="Try Clicking me!!")
label1.place(x=225, y=10)

button = ttk.Button(root, text="Click me", command=randomLocation)
button.place(x=225, y=50)

if __name__ == "__main__":
    root.mainloop()