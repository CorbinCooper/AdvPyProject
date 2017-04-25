# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 16:14:04 2017
@author: Robert
"""

import tkinter as tk   # python3
#import Tkinter as tk   # python

from tkinter import*

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
        for F in (StartPage, oneDmotion, Kinematics, Newton2nd, EM, CoulombsLaw, OhmsLaw, GuassLaw, LorentzForce, Resistivity, Conductivity):
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
       
        lbl_new = tk.Label(self, width = 35, text = "Newton's laws of motion are\nthree physical laws that describe\nthe relationship between a body and\nthe forces acting upon it, and its\nm.otion in response to those forces.")
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

    def Fmenu(*args):
        if Ftype.get() == "Generic":
            menu_SolveFor = tk.OptionMenu(self, find, "Force", "Mass", "Acceleration")
            menu_SolveFor.grid(row=5, column=4, padx = 5, pady = 5)

        elif Ftype.get() == "Gravity":
            menu_SolveFor = tk.OptionMenu(self, find, "Force", "Mass", "Gravity")
            menu_SolveFor.grid(row=5, column=4, padx = 5, pady = 5)

        else:
            print('')
 

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        units = IntVar()
        units.set(1)
        find = StringVar()
        Ftype = StringVar()
        Ftype.set("Generic")
        
        lbl_title = tk.Label(self, text="Newton's 2nd Law", font=TITLE_FONT)
        lbl_title.grid(row=1, column=3, padx=20)

        rbut_metric = tk.Radiobutton(self, text="Metric Units", variable = units, value=1)
        rbut_metric.grid(row=3, column=3, padx = 5, pady = 5)

        rbut_english = tk.Radiobutton(self, text="English Units", variable = units, value=2)
        rbut_english.grid(row=3, column=4, padx = 5, pady = 5)

        lbl_Ftype = tk.Label(self, text="Force type :  ")
        lbl_Ftype.grid(row=4, column=3, padx = 5, pady = 5)

        menu_Ftype = tk.OptionMenu(self, Ftype, "Generic", "Gravity", "Spring", "Friction", "Pressure")
        menu_Ftype.grid(row=4, column=4, padx = 5, pady = 5)
    

        lbl_SolveFor = tk.Label(self, text="Solve for :  ")
        lbl_SolveFor.grid(row=5, column=3, padx = 5, pady = 5)

        but_solve = tk.Button(self, text="SOLVE")
        but_solve.grid(row=8, column=4)

        lbl_Atype = tk.Label(self, text='')
        lbl_Atype.grid(row=9, column=3) 
        lbl_ans = tk.Label(self, text='')
        lbl_ans.grid(row=9, column=4)


        def Fmenu(*args):
            if Ftype.get() == "Generic":
                menu_SolveFor = tk.OptionMenu(self, find, "Force", "Mass", "Acceleration")
                menu_SolveFor.grid(row=5, column=4, padx = 5, pady = 5)
                find.set("Force")

            elif Ftype.get() == "Gravity":
                menu_SolveFor = tk.OptionMenu(self, find, "Weight", "Mass", "Gravity")
                menu_SolveFor.grid(row=5, column=4, padx = 5, pady = 5)
                find.set("Weight")

            elif Ftype.get() == "Spring":
                menu_SolveFor = tk.OptionMenu(self, find, "Spring Force", "Spring Constant", "Displacement")
                menu_SolveFor.grid(row=5, column=4, padx = 5, pady = 5)
                find.set("Spring Force")

            elif Ftype.get() == "Friction":
                menu_SolveFor = tk.OptionMenu(self, find, "Friction Force", "Friction Coefficient", "Normal Force")
                menu_SolveFor.grid(row=5, column=4, padx = 5, pady = 5)
                find.set("Friction Force")

            elif Ftype.get() == "Pressure":
                menu_SolveFor = tk.OptionMenu(self, find, "Force", "Pressure", "Area")
                menu_SolveFor.grid(row=5, column=4, padx = 5, pady = 5)
                find.set("Force")
                
            else:
                print('')
    

        def entry_fields(*args):

            label1 = Label(self)
            label2 = Label(self)
            
            label1.grid_remove()
            label2.grid_remove()

            label1.grid(row=6, column=3, sticky=E)
            label2.grid(row=7, column=3, sticky=E)        
            
            if Ftype.get() == "Generic":
                if find.get() == "Force":
                    label1.config(text="               Mass (kg): ")
                    mass = Entry(self)
                    mass.grid(row=6, column=4)
                    label2.config(text="Acceleration (m/s^2): ")
                    accel = Entry(self)
                    accel.grid(row=7, column=4)
                    but_solve.config(command = Gen_Force())
                elif find.get() == "Mass":
                    label1.config(text="Force (N): ")
                    force = Entry(self)
                    force.grid(row=6, column=4)
                    label2.config(text="Acceleration (m/s^2): ")
                    accel = Entry(self)
                    accel.grid(row=7, column=4)
                elif find.get() == "Acceleration":
                    label1.config(text="Force (N): ")
                    force = Entry(self)
                    force.grid(row=6, column=4)
                    label2.config(text="                       Mass (kg):")
                    mass = Entry(self)
                    mass.grid(row=7, column=4)
                else:
                    print('')

            if Ftype.get() == "Gravity":
                if find.get() == "Weight":
                    label1.config(text="                   Mass (kg): ")
                    mass = Entry(self)
                    mass.grid(row=6, column=4)
                    label2.config(text="       Gravity (m/s^2): ")
                    grav = Entry(self)
                    grav.grid(row=7, column=4)
                elif find.get() == "Mass":
                    label1.config(text="Weight (N): ")
                    weight = Entry(self)
                    weight.grid(row=6, column=4)
                    label2.config(text="       Gravity (m/s^2): ")
                    grav = Entry(self)
                    grav.grid(row=7, column=4)
                elif find.get() == "Gravity":
                    label1.config(text="Weight (N): ")
                    weight = Entry(self)
                    weight.grid(row=6, column=4)
                    label2.config(text="                       Mass (kg):")
                    mass = Entry(self)
                    mass.grid(row=7, column=4)
                else:
                    print('')

            if Ftype.get() == "Spring":
                if find.get() == "Spring Force":
                    label1.config(text="Spring Constant: ")
                    cons = Entry(self)
                    cons.grid(row=6, column=4)
                    label2.config(text="Displacement (m): ")
                    disp = Entry(self)
                    disp.grid(row=7, column=4)
                elif find.get() == "Spring Constant":
                    label1.config(text="Spring Force (N): ")
                    force = Entry(self)
                    force.grid(row=6, column=4)
                    label2.config(text="Displacement (m): ")
                    disp = Entry(self)
                    disp.grid(row=7, column=4)
                elif find.get() == "Displacement":
                    label1.config(text="Spring Force (N): ")
                    force = Entry(self)
                    force.grid(row=6, column=4)
                    label2.config(text="       Spring Constant:")
                    cons = Entry(self)
                    cons.grid(row=7, column=4)
                else:
                    print('')

            if Ftype.get() == "Friction":
                if find.get() == "Friction Force":
                    label1.config(text="     Friction Coefficient: ")
                    coeff = Entry(self)
                    coeff.grid(row=6, column=4)
                    label2.config(text="     Normal Force (N): ")
                    norm = Entry(self)
                    norm.grid(row=7, column=4)
                elif find.get() == "Friction Coefficient":
                    label1.config(text="     Friction Force (N): ")
                    force = Entry(self)
                    force.grid(row=6, column=4)
                    label2.config(text="     Normal Force (N): ")
                    norm = Entry(self)
                    norm.grid(row=7, column=4)
                elif find.get() == "Normal Force":
                    label1.config(text="     Friction Force (N): ")
                    force = Entry(self)
                    force.grid(row=6, column=4)
                    label2.config(text="    Friction Coefficient:")
                    coeff = Entry(self)
                    coeff.grid(row=7, column=4)
                else:
                    print('')

            if Ftype.get() == "Pressure":
                if find.get() == "Force":
                    label1.config(text="     Pressure (Pa): ")
                    press = Entry(self)
                    press.grid(row=6, column=4)
                    label2.config(text="     Area (m^2): ")
                    area = Entry(self)
                    area.grid(row=7, column=4)
                elif find.get() == "Pressure":
                    label1.config(text="          Force (N): ")
                    force = Entry(self)
                    force.grid(row=6, column=4)
                    label2.config(text="            Area (m^2): ")
                    area = Entry(self)
                    area.grid(row=7, column=4)
                elif find.get() == "Area":
                    label1.config(text="     Force (N): ")
                    force = Entry(self)
                    force.grid(row=6, column=4)
                    label2.config(text="    Pressure (Pa):")
                    press = Entry(self)
                    press.grid(row=7, column=4)
                else:
                    print('')

            else:
                print('')

        def Gen_Force():
            mass = mass.get()
            accel = accel.get()

            force = mass * accel
            lbl_Atype.config(text="Force = ")
            lbl_ans.config(force, " N")
    
        Ftype.trace("w", Fmenu)
        find.trace("w", entry_fields)

        button = tk.Button(self, text="Go to the home page",
                           command=lambda: controller.show_frame("StartPage"))
        button.grid(row=10, column=3)

        bt_button = tk.Button(self, text = 'EXIT', fg = 'red', bg = 'light grey', command = exit)
        bt_button.grid(row=10, column=4)

class EM(tk.Frame): #Home page for Electromagnetism

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Electromagnetism", font=TITLE_FONT)
        label.grid(row=0, column=2, pady = 10)
        button1 = tk.Button(self, text="Coulomb's Law", width=16,
                           command=lambda: controller.show_frame("CoulombsLaw"))
        button2 = tk.Button(self, text="Ohm's Law", width=16,
                           command=lambda: controller.show_frame("OhmsLaw"))
        button3 = tk.Button(self, text="Gauss' Law", width=16,
                           command=lambda: controller.show_frame("GuassLaw"))
        button4 = tk.Button(self, text="Lorentz Force", width=16,
                           command=lambda: controller.show_frame("LorentzForce"))
        button5 = tk.Button(self, text="Resistivity", width=16,
                           command=lambda: controller.show_frame("Resistivity"))
        button6 = tk.Button(self, text="Conductivity", width=16,
                           command=lambda: controller.show_frame("Conductivity"))
        button1.grid(row=2, column=1, padx = 5, pady = 5)
        button2.grid(row=2, column=2, padx = 5)
        button3.grid(row=2, column=3, padx = 5)
        button4.grid(row=3, column=1, padx = 5, pady = 5)
        button5.grid(row=3, column=2, padx = 5)
        button6.grid(row=3, column=3, padx = 5)
        button = tk.Button(self, text="Back",
                           command=lambda: controller.show_frame("StartPage"))
        button.grid(row=5, column=1, pady = 10)
        bt_button = tk.Button(self, text = 'EXIT', fg = 'red', bg = 'light grey', command = exit)
        bt_button.grid(row=5, column=2, pady = 10)


class CoulombsLaw(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Coulomb's Law", font=TITLE_FONT)
        label.grid(row=0, column=2, pady = 10)      
        
        label1 = tk.Label(self, text="Force")
        label1.grid(row=1, column=3, pady = 10)
        label2 = tk.Label(self, text="Electric Field")
        label2.grid(row=1, column=7, pady = 10)
        entry1 = tk.Entry(self)       
        entry1.grid(row=2, column=3, pady = 10)
        labe2 = tk.Label(self, text="Charge (q) 1")
        labe2.grid(row=2, column=2, pady = 10)
        
        entry2 = tk.Entry(self)       
        entry2.grid(row=3, column=3, pady = 10)
        labe3 = tk.Label(self, text="Charge (q) 2")
        labe3.grid(row=3, column=2, pady = 10)
        
        entry3 = tk.Entry(self)       
        entry3.grid(row=4, column=3, pady = 10)
        labe4 = tk.Label(self, text="Radius (r)")
        labe4.grid(row=4, column=2, pady = 10)
        
        entry4 = tk.Entry(self)       
        entry4.grid(row=2, column=7, pady = 10)
        labe3 = tk.Label(self, text="Charge (q)")
        labe3.grid(row=2, column=6, pady = 10)
        
        entry5 = tk.Entry(self)       
        entry5.grid(row=3, column=7, pady = 10)
        labe6 = tk.Label(self, text="Radius (r)")
        labe6.grid(row=3, column=6, pady = 10)
        
        buttonCalcF = tk.Button(self, text="Calculate F",
                           command=lambda: Print(4))
        buttonCalcF.grid(row=5, column=3, pady = 10)
        buttonCalcE = tk.Button(self, text="Calculate E",
                           command=lambda: Print(4))
        buttonCalcE.grid(row=5, column=7, pady = 10)
        
        bt_button = tk.Button(self, text = 'EXIT', fg = 'red', bg = 'light grey', command = exit)
        bt_button.grid(row=6, column=4, pady = 10)
        button = tk.Button(self, text="Back",
                           command=lambda: controller.show_frame("EM"))
        button.grid(row=6, column=2, pady = 10)
    def showEntryFields():
        print(5)
        
class OhmsLaw(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Ohm's Law", font=TITLE_FONT)
        label.grid(row=0, column=2, pady = 10)

        label1 = tk.Label(self, text="Volyage (V)")
        label1.grid(row=1, column=3, pady = 10)
        label2 = tk.Label(self, text="Current (I)")
        label2.grid(row=1, column=7, pady = 10)
        entry1 = tk.Entry(self)       
        entry1.grid(row=2, column=3, pady = 10)
        labe2 = tk.Label(self, text="Current (I)")
        labe2.grid(row=2, column=2, pady = 10)
        
        entry2 = tk.Entry(self)       
        entry2.grid(row=3, column=3, pady = 10)
        labe3 = tk.Label(self, text="Resistance (R)")
        labe3.grid(row=3, column=2, pady = 10)
        
        entry4 = tk.Entry(self)       
        entry4.grid(row=2, column=7, pady = 10)
        labe3 = tk.Label(self, text="Voltage (V)")
        labe3.grid(row=2, column=6, pady = 10)
        
        entry5 = tk.Entry(self)       
        entry5.grid(row=3, column=7, pady = 10)
        labe6 = tk.Label(self, text="Resistance (R)")
        labe6.grid(row=3, column=6, pady = 10)
        buttonCalcF = tk.Button(self, text="Calculate V",
                           command=lambda: Print(4))
        buttonCalcF.grid(row=5, column=3, pady = 10)
        buttonCalcE = tk.Button(self, text="Calculate I",
                           command=lambda: Print(4))
        buttonCalcE.grid(row=5
                         , column=7, pady = 10)

        button = tk.Button(self, text="Back",
                           command=lambda: controller.show_frame("EM"))
        button.grid(row=6, column=3, pady = 10)
     
        bt_button = tk.Button(self, text = 'EXIT', fg = 'red', bg = 'light grey', command = exit)
        bt_button.grid(row=6, column=4, pady = 10)

class GuassLaw(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Guass' Law", font=TITLE_FONT)
        label.grid(row=0, column=2, pady = 10)
        button = tk.Button(self, text="Back",
                           command=lambda: controller.show_frame("EM"))
        button.grid(row=2, column=2, pady = 10)
        
        bt_button = tk.Button(self, text = 'EXIT', fg = 'red', bg = 'light grey', command = exit)
        bt_button.grid(row=5, column=2, pady = 10)

class LorentzForce(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Lorentz Force", font=TITLE_FONT)
        label.grid(row=0, column=2, pady = 10)
        button = tk.Button(self, text="Back",
                           command=lambda: controller.show_frame("EM"))
        button.grid(row=2, column=2, pady = 10)
        
        bt_button = tk.Button(self, text = 'EXIT', fg = 'red', bg = 'light grey', command = exit)
        bt_button.grid(row=5, column=2, pady = 10)

class Resistivity(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Resistivity", font=TITLE_FONT)
        label.grid(row=0, column=2, pady = 10)
        button = tk.Button(self, text="Back",
                           command=lambda: controller.show_frame("EM"))
        button.grid(row=2, column=2, pady = 10)
        
        bt_button = tk.Button(self, text = 'EXIT', fg = 'red', bg = 'light grey', command = exit)
        bt_button.grid(row=5, column=2, pady = 10)

class Conductivity(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Conductivity", font=TITLE_FONT)
        label.grid(row=0, column=2, pady = 10)
        button = tk.Button(self, text="Back",
                           command=lambda: controller.show_frame("EM"))
        button.grid(row=2, column=2, pady = 10)
        
        bt_button = tk.Button(self, text = 'EXIT', fg = 'red', bg = 'light grey', command = exit)
        bt_button.grid(row=5, column=2, pady = 10)

if __name__ == "__main__": 
    app = PhysSolv()
    app.mainloop()
    
