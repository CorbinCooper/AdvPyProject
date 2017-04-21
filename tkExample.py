# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 15:30:03 2017

@author: Robert

Saving Stuff
Use pickle
"""

import tkinter as tk

root = tk.Tk()

root.configure(bg="white")

root.title('Physics Solver')

#root.geometry("350x300")

#Functions
def someFun(name, label):
    label.config(text = 'Hello ' + name)


#code and buttons go here
label = tk.Label(root, text = '', fg = 'green', bg = 'white')
label.grid(row=1, column=0)

lbl_entName = tk.Label(root, text = 'Enter your name: ', fg = 'green', bg = 'white')
lbl_entName.grid(row=2, column=0)

en_entName = tk.Entry(root, width = 20)
en_entName.grid(row=2, column=1)

bt_entName = tk.Button(root, text = 'Enter', fg = 'green', bg = 'grey', command = lambda: someFun(en_entName.get(), label))
#bt_entName.grid(row=2, column=2)

bt_button = tk.Button(root, text = 'EXIT', fg = 'red', bg = 'grey', command = exit)
#bt_button.grid(row=5, column=0)





#stays at end
root.mainloop()
