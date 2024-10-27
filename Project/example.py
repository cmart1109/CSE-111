from tkinter import *
root = Tk()
var = StringVar()
label = Message(root, anchor="center", textvariable=var, relief=FLAT, padx="40")
var.set("Hey!? How are you Doing?")
label.pack()
root.mainloop()