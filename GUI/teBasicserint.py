import tkinter as tk
from tefuntions import *
#from dotenv import load_dotenv
#import requests
#import os
#import json

root = tk.Tk()

root.geometry('640x480+300+300')
root.resizable(True, True)
root.title("Thousand Eyes GUI")

title = tk.Label(
  root,
  text='Basic GUI to get EN agents',
  font=('Arial 16 bold'),
)

name_label = tk.Label(root, text='What is the information you require?')

user_inp = tk.Listbox(root, height=3)  # Only show selected item
# add choices
user_choices = (
  'Enterprise agents', 'Rules', "Both"
  )
for choice in user_choices:
  user_inp.insert(tk.END, choice)

token_label = tk.Label(root, text="PLease enter your authentication token")
token_entry = tk.Entry(root)

submit_btn = tk.Button(root, text='Get information')
output_line = tk.Label(root, text='', anchor='w', justify='center')

title.grid()
name_label.grid(row=1, column=0)
user_inp.grid(row=2,columnspan=2,sticky='we',padx=10)
token_label.grid(row=3,columnspan=1, stick="e",ipadx=10, ipady=5)
token_entry.grid(row=4, columnspan=1, ipadx=50, ipady=5, padx=5, pady=5)
submit_btn.grid(row=6, column=1,ipadx=10, ipady=5, padx=5, pady=5)
output_line.grid(row=100,sticky="NSEW",ipadx=10, ipady=20)

root.columnconfigure(1,weight=1)
root.rowconfigure(99, weight=2)
root.rowconfigure(100,weight=1)

def on_submit():

    user_select = user_inp.curselection()
    if user_select:
        selection = user_inp.get(user_select)
        if selection == "Enterprise agents":
            print("hola")
            try:
                dict = list_ENagents(token_entry.get())
                if dict["code"] == 200:
                    message = dict["message"]
                    output_line.configure(text=message)

            except:
                output_line.configure(text="There was an error with the Auth token")
        if selection == "Rules":
            print("Adios")
            message = ("adios")
            output_line.configure(text=message)
        if selection == "Both":
            message = ("not configure")
            print("No configure yet")
            output_line.configure(text=message)
    else:
        selection = ""

submit_btn.configure(command=on_submit)

root.mainloop()
