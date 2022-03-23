#imprt tk module
import tkinter as tk

#main window

root = tk.Tk()

#Title
root.title("ThousandEyes GUI")
#first label
label = tk.Label(root, text="Hello World")

#pack Label

label.pack()

#starting loop

root.mainloop()
