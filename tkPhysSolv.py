# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 16:14:04 2017

@author: Robert
"""

import tkinter as tk   # python3
#import Tkinter as tk   # python

TITLE_FONT = ("Helvetica", 18, "bold")



class PhysSolv(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        self.title('Physics Solver')        
        
        
        self.frames = {}
        for F in (StartPage, oneDmotion, Kinematics, Newton2nd, EM):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()
        

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Home", font=TITLE_FONT)
        label.grid(row=0, column=1, pady = 10)

        
        button1 = tk.Button(self, text="One-Dimensional Motion", width=25,
                            command=lambda: controller.show_frame("oneDmotion"))
        button2 = tk.Button(self, text="Newton's 2nd Law", width=16,
                            command=lambda: controller.show_frame("Newton2nd"))
        button3 = tk.Button(self, text="Electromagnetism", width=16,
                            command=lambda: controller.show_frame("EM"))
 
        lbl_kine = tk.Label(self, width = 35, text = "One-dimensional motion uses\nmathematics to describe motion \nof an object.")
        lbl_kine.grid(row=1,column=0, padx = 5, pady = 5)
       
        lbl_new = tk.Label(self, width = 35, text = "Here is some stuff \n about Newton's 2nd Law")
        lbl_new.grid(row=1,column=1, padx = 5)
        
        lbl_em = tk.Label(self, width = 35, text = "Electromagnetism is a branch of\nphysics involving the study\nof the electromagnetic \nforce, a type of physical\ninteraction that occurs between\nelectrically charged particles.")
        lbl_em.grid(row=1,column=2, padx = 5)

        button1.grid(row=2, column=0, padx = 5, pady = 5)
        button2.grid(row=2, column=1, padx = 5)
        button3.grid(row=2, column=2, padx = 5)
        
        bt_button = tk.Button(self, text = 'EXIT', fg = 'red', bg = 'light grey', command = exit)
        bt_button.grid(row=3, column=1, pady = 10)        
        

class oneDmotion(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="One-Dimensional Motion", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the home page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()
        
        bt_button = tk.Button(self, text = 'EXIT', fg = 'red', bg = 'light grey', command = exit)
        bt_button.pack(side="bottom", pady = 20)
        
class Kinematics(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Kinematics", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the home page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()
        
        bt_button = tk.Button(self, text = 'EXIT', fg = 'red', bg = 'light grey', command = exit)
        bt_button.pack(side="bottom", pady = 20)
        
        

class Newton2nd(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Newton's 2nd Law", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the home page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()

        bt_button = tk.Button(self, text = 'EXIT', fg = 'red', bg = 'light grey', command = exit)
        bt_button.pack(side="bottom", pady = 20)

class EM(tk.Frame): #Home page for Electromagnetism

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Electromagnetism", font=TITLE_FONT)
        label.grid(row=0, column=2, pady = 10)
        button1 = tk.Button(self, text="Coulomb's Law", width=16,
                           command=lambda: controller.show_frame("StartPage"))
        button2 = tk.Button(self, text="Ohm's Law", width=16,
                           command=lambda: controller.show_frame("StartPage"))
        button3 = tk.Button(self, text="Gauss' Law", width=16,
                           command=lambda: controller.show_frame("StartPage"))
        button4 = tk.Button(self, text="Lorentz Force", width=16,
                           command=lambda: controller.show_frame("StartPage"))
        button5 = tk.Button(self, text="Resistivity", width=16,
                           command=lambda: controller.show_frame("StartPage"))
        button6 = tk.Button(self, text="Conductivity", width=16,
                           command=lambda: controller.show_frame("StartPage"))
        button1.grid(row=2, column=1, padx = 5, pady = 5)
        button2.grid(row=2, column=2, padx = 5)
        button3.grid(row=2, column=3, padx = 5)
        button4.grid(row=3, column=1, padx = 5, pady = 5)
        button5.grid(row=3, column=2, padx = 5)
        button6.grid(row=3, column=3, padx = 5)
        bt_button = tk.Button(self, text = 'EXIT', fg = 'red', bg = 'light grey', command = exit)
        bt_button.grid(row=5, column=2, pady = 10)


if __name__ == "__main__": 
    app = PhysSolv()
    app.mainloop()
    
