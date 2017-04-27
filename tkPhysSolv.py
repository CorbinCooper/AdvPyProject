# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 16:14:04 2017
@author: Robert Millican, Eric Hartline, Corbin Cooper
"""

import tkinter as tk   # python3
#import Tkinter as tk   # python
import math

TITLE_FONT = ("Helvetica", 18, "bold")
SUB_FONT = ("Helvetica", 14, 'bold' )


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
        for F in (StartPage, oneDmotion, Kinematics, Momentum, FreeFall, Newton2nd, EM, CoulombsLaw, OhmsLaw, GuassLaw, LorentzForce, Resistivity, Conductivity):
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
       
        lbl_new = tk.Label(self, width = 35, text = "Solve systems that use force,\n mass, and acceleration to analyze\n an object's motion.")
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
        label.grid(row=0,  column=1, pady=10)
        
        lb_kine = tk.Label(self, font=SUB_FONT, text='Kinematics')
        lb_kine.grid(row=1,column=0)        
    
        button = tk.Button(self, border = '3', text="Back to the home page",
                           command=lambda: controller.show_frame("StartPage"))
        button.grid(row=3,column=0)
    
        bt_button = tk.Button(self, text = 'EXIT', fg = 'red', bg = 'light grey', command = exit)
        bt_button.grid(row=3,column=3)
        
class Kinematics(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Kinematics", font=TITLE_FONT)
        label.grid(row=0, column=2, columnspan = 2, pady=10)
        button = tk.Button(self, border = '3', text="Back to the home page",
                           command=lambda: controller.show_frame("StartPage"))
        button.grid(row=15, column=0)
        
        bt_button = tk.Button(self, text = 'EXIT', fg = 'red', bg = 'light grey', command = exit)
        bt_button.grid(row=15,column=3)
        
class Momentum(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Momentum", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, border = '3', text="Back to the home page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()
        
        bt_button = tk.Button(self, text = 'EXIT', fg = 'red', bg = 'light grey', command = exit)
        bt_button.pack(side="bottom", pady = 20)
        
class FreeFall(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Free Fall", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, border = '3', text="Back to the home page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()
        
        bt_button = tk.Button(self, text = 'EXIT', fg = 'red', bg = 'light grey', command = exit)
        bt_button.pack(side="bottom", pady = 20)

class Newton2nd(tk.Frame):


    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        units = tk.IntVar()
        units.set(1)
        find = tk.StringVar()
        Ftype = tk.StringVar()
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


    
        label1 = tk.Label(self)
        label2 = tk.Label(self)

        label1.grid(row=6, column=3, sticky='e')
        label2.grid(row=7, column=3, sticky='e')

        def entry_fields(*args):

            label1.config(text="                          ")
            label2.config(text="                          ")
            lbl_Atype.config(text="                          ")
            lbl_ans.config(text="                          ")

            if Ftype.get() == "Generic":
                if find.get() == "Force":
                    label1.config(text="Mass (kg): ")
                    mass = tk.Entry(self)
                    mass.grid(row=6, column=4)
                    label2.config(text="Acceleration (m/s^2): ")
                    accel = tk.Entry(self)
                    accel.grid(row=7, column=4)
                    but_solve.config(command = lambda: Gen_Force(float(mass.get()),float(accel.get())))
                    
                elif find.get() == "Mass":
                    label1.config(text="Force (N): ")
                    force = tk.Entry(self)
                    force.grid(row=6, column=4)
                    label2.config(text="Acceleration (m/s^2): ")
                    accel = tk.Entry(self)
                    accel.grid(row=7, column=4)
                    but_solve.config(command = lambda: Gen_Mass(float(force.get()),float(accel.get())))

                    
                elif find.get() == "Acceleration":
                    label1.config(text="Force (N): ")
                    force = tk.Entry(self)
                    force.grid(row=6, column=4)
                    label2.config(text="Mass (kg):")
                    mass = tk.Entry(self)
                    mass.grid(row=7, column=4)
                    but_solve.config(command = lambda: Gen_Accel(float(force.get()),float(mass.get())))
                    
                else:
                    print('')

            if Ftype.get() == "Gravity":
                if find.get() == "Weight":
                    label1.config(text="Mass (kg): ")
                    mass = tk.Entry(self)
                    mass.grid(row=6, column=4)
                    label2.config(text="Gravity (m/s^2): ")
                    grav = tk.Entry(self)
                    grav.grid(row=7, column=4)
                    but_solve.config(command = lambda: Grav_Weight(float(mass.get()),float(grav.get())))
                    
                elif find.get() == "Mass":
                    label1.config(text="Weight (N): ")
                    weight = tk.Entry(self)
                    weight.grid(row=6, column=4)
                    label2.config(text="Gravity (m/s^2): ")
                    grav = tk.Entry(self)
                    grav.grid(row=7, column=4)
                    but_solve.config(command = lambda: Grav_Mass(float(weight.get()),float(grav.get())))
                    
                elif find.get() == "Gravity":
                    label1.config(text="Weight (N): ")
                    weight = tk.Entry(self)
                    weight.grid(row=6, column=4)
                    label2.config(text="Mass (kg):")
                    mass = tk.Entry(self)
                    mass.grid(row=7, column=4)
                    but_solve.config(command = lambda: Grav_Grav(float(weight.get()),float(mass.get())))
                    
                else:
                    print('')


            if Ftype.get() == "Spring":
                if find.get() == "Spring Force":
                    label1.config(text="Spring Constant: ")
                    cons = tk.Entry(self)
                    cons.grid(row=6, column=4)
                    label2.config(text="Displacement (m): ")
                    disp = tk.Entry(self)
                    disp.grid(row=7, column=4)
                    but_solve.config(command = lambda: Spring_Force(float(cons.get()),float(disp.get())))

                    
                elif find.get() == "Spring Constant":
                    label1.config(text="Spring Force (N): ")
                    force = tk.Entry(self)
                    force.grid(row=6, column=4)
                    label2.config(text="Displacement (m): ")
                    disp = tk.Entry(self)
                    disp.grid(row=7, column=4)
                    but_solve.config(command = lambda: Spring_Cons(float(force.get()),float(disp.get())))

                    
                elif find.get() == "Displacement":
                    label1.config(text="Spring Force (N): ")
                    force = tk.Entry(self)
                    force.grid(row=6, column=4)
                    label2.config(text="Spring Constant:")
                    cons = tk.Entry(self)
                    cons.grid(row=7, column=4)
                    but_solve.config(command = lambda: Spring_Disp(float(force.get()),float(cons.get())))

                    
                else:
                    print('')

            if Ftype.get() == "Friction":
                if find.get() == "Friction Force":
                    label1.config(text="Friction Coefficient: ")
                    coeff = tk.Entry(self)
                    coeff.grid(row=6, column=4)
                    label2.config(text="Normal Force (N): ")
                    norm = tk.Entry(self)
                    norm.grid(row=7, column=4)
                    but_solve.config(command = lambda: Fric_Force(float(coeff.get()),float(norm.get())))
                    
                elif find.get() == "Friction Coefficient":
                    label1.config(text="Friction Force (N): ")
                    force = tk.Entry(self)
                    force.grid(row=6, column=4)
                    label2.config(text="Normal Force (N): ")
                    norm = tk.Entry(self)
                    norm.grid(row=7, column=4)
                    but_solve.config(command = lambda: Fric_Coeff(float(force.get()),float(norm.get())))
                    
                elif find.get() == "Normal Force":
                    label1.config(text="Friction Force (N): ")
                    force = tk.Entry(self)
                    force.grid(row=6, column=4)
                    label2.config(text="Friction Coefficient:")
                    coeff = tk.Entry(self)
                    coeff.grid(row=7, column=4)
                    but_solve.config(command = lambda: Fric_Norm(float(force.get()),float(coeff.get())))
                    
                else:
                    print('')

            if Ftype.get() == "Pressure":
                if find.get() == "Force":
                    label1.config(text="Pressure (Pa): ")
                    press = tk.Entry(self)
                    press.grid(row=6, column=4)
                    label2.config(text="Area (m^2): ")
                    area = tk.Entry(self)
                    area.grid(row=7, column=4)
                    but_solve.config(command = lambda: Press_Force(float(press.get()),float(area.get())))
                    
                elif find.get() == "Pressure":
                    label1.config(text="Force (N): ")
                    force = tk.Entry(self)
                    force.grid(row=6, column=4)
                    label2.config(text="Area (m^2): ")
                    area = tk.Entry(self)
                    area.grid(row=7, column=4)
                    but_solve.config(command = lambda: Press_Press(float(force.get()),float(area.get())))
                    
                elif find.get() == "Area":
                    label1.config(text=" Force (N): ")
                    force = tk.Entry(self)
                    force.grid(row=6, column=4)
                    label2.config(text="Pressure (Pa):")
                    press = tk.Entry(self)
                    press.grid(row=7, column=4)
                    but_solve.config(command = lambda: Press_Area(float(force.get()),float(area.get())))
                    
                else:
                    print('')

            else:
                print('')

        def Gen_Force(mass, accel):
            force = mass * accel
            lbl_Atype.config(text="Force = ")
            lbl_ans.config(text = str(force) + " N")

        def Gen_Mass(force, accel):
            mass = force / accel
            lbl_Atype.config(text="Mass = ")
            lbl_ans.config(text = str(mass) + " kg")            

        def Gen_Accel(force, mass):
            accel = force / mass
            lbl_Atype.config(text="Acceleration = ")
            lbl_ans.config(text = str(accel) + " m/s^2")

        def Grav_Weight(mass, grav):
            weight = mass * grav
            lbl_Atype.config(text="Weight = ")
            lbl_ans.config(text = str(weight) + " N")

        def Grav_Mass(weight, grav):
            mass = weight / grav
            lbl_Atype.config(text="Mass = ")
            lbl_ans.config(text = str(mass) + " kg")

        def Grav_Grav(weight, mass):
            grav = weight / mass
            lbl_Atype.config(text="Gravity = ")
            lbl_ans.config(text = str(grav) + " m/s^2")

        def Spring_Force(cons, disp):
            force = cons*disp
            lbl_Atype.config(text="Spring Force = ")
            lbl_ans.config(text = str(force) + " N")
            
        def Spring_Disp(force, cons):
            disp = force / cons
            lbl_Atype.config(text="Displacement = ")
            lbl_ans.config(text = str(disp) + " m")
            
        def Spring_Cons(force, disp):
            cons = force / disp
            lbl_Atype.config(text="Spring Constant = ")
            lbl_ans.config(text = str(cons))
            
        def Fric_Force(coeff, norm):
            force = coeff*norm
            lbl_Atype.config(text="Friction Force = ")
            lbl_ans.config(text = str(force) + " N")
            
        def Fric_Coeff(force, norm):
            coeff = force / norm
            lbl_Atype.config(text="Friction Coefficient = ")
            lbl_ans.config(text = str(coeff))
            
        def Fric_Norm(force, coeff):
            norm = force / coeff
            lbl_Atype.config(text="Normal Force = ")
            lbl_ans.config(text = str(norm) + " N")

        def Press_Force(press, area):
            force = press*area
            lbl_Atype.config(text="Force = ")
            lbl_ans.config(text = str(force) + " N")
            
        def Press_Press(force, area):
            press = force / area
            lbl_Atype.config(text="Pressure = ")
            lbl_ans.config(text = str(press) + " Pa")
            
        def Press_Area(force, press):
            area = force / press
            lbl_Atype.config(text="Area = ")
            lbl_ans.config(text = str(area) + " m^2")            
    
        Ftype.trace("w", Fmenu)
        find.trace("w", entry_fields)

        button = tk.Button(self, border = '3', text="Back to the home page",
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
        button = tk.Button(self, text="Back to the Home Page",
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
        q1 = tk.Entry(self)       
        q1.grid(row=2, column=3, pady = 10)
        labe2 = tk.Label(self, text="Charge 1 (e)")
        labe2.grid(row=2, column=2, pady = 10)
        
        q2 = tk.Entry(self)       
        q2.grid(row=3, column=3, pady = 10)
        labe3 = tk.Label(self, text="Charge 2 (e)")
        labe3.grid(row=3, column=2, pady = 10)
        
        r = tk.Entry(self)       
        r.grid(row=4, column=3, pady = 10)
        labe4 = tk.Label(self, text="Radius (m)")
        labe4.grid(row=4, column=2, pady = 10)
        
        q = tk.Entry(self)       
        q.grid(row=2, column=8, pady = 10)
        labe5 = tk.Label(self, text="Charge (e)")
        labe5.grid(row=2, column=7, pady = 10)
        
        radius = tk.Entry(self)       
        radius.grid(row=3, column=8, pady = 10)
        labe6 = tk.Label(self, text="Radius (m)")
        labe6.grid(row=3, column=7, pady = 10)
        
        buttonCalcF = tk.Button(self, text="Calculate F")
        buttonCalcF.grid(row=5, column=3, pady = 10)
        buttonCalcF.config(command=lambda: calc_coulombs_force(float(q1.get()), float(q2.get()), float(r.get())))
                           
        buttonCalcE = tk.Button(self, text="Calculate E")
        buttonCalcE.grid(row=5, column=8, pady = 10)
        buttonCalcE.config(command=lambda: calc_coulombs_electric(float(q.get()), float(radius.get())))
        
        bt_button = tk.Button(self, text = 'EXIT', fg = 'red', bg = 'light grey', command = exit)
        bt_button.grid(row=7, column=4, pady = 10)
        button = tk.Button(self, text="Back to Options Menu",
                           command=lambda: controller.show_frame("EM"))
        button.grid(row=7, column=2, pady = 10)

        ansF_text = tk.Label(self, text='')
        ansF_text.grid(row=6, column=2) 
        ansF = tk.Label(self, text='')
        ansF.grid(row=6, column=3)

        ansE_text = tk.Label(self, text='')
        ansE_text.grid(row=6, column=5, columnspan = 2) 
        ansE = tk.Label(self, text='')
        ansE.grid(row=6, column=6, columnspan = 3)
        
        def calc_coulombs_force(q1, q2, r):
            e = 1.602177*10**(-19)
            force = (1/(4*math.pi*8.854*10**(-12)))*(q1*e*q2*e/r**2)
            ansF_text.config(text="Force     = ")
            ansF.config(text = str(force) + " N")
        def calc_coulombs_electric(q, radius):
            e = 1.602177*10**(-19)
            force = (1/(4*math.pi*8.854*10**(-12)))*(q*e/radius**2)
            ansE_text.config(text="Electric Field     = ")
            ansE.config(text = str(force) + " N/C")
            
class OhmsLaw(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller        

        
        
        label = tk.Label(self, text="Ohm's Law", font=TITLE_FONT)
        label.grid(row=0, column=2, pady = 10)      
        
        label1 = tk.Label(self, text="Potential (V)")
        label1.grid(row=1, column=3, pady = 10)
        
        I = tk.Entry(self)       
        I.grid(row=2, column=3, pady = 10)

        labe2 = tk.Label(self, text="Current (I)")
        labe2.grid(row=2, column=2, pady = 10)
        
        R1 = tk.Entry(self)       
        R1.grid(row=3, column=3, pady = 10)
        labe3 = tk.Label(self, text="Resistance (Ω)")
        labe3.grid(row=3, column=2, pady = 10)

        label2 = tk.Label(self, text="Current (I)")
        label2.grid(row=1, column=8, pady = 10)
        
        V = tk.Entry(self)       
        V.grid(row=2, column=8, pady = 10)
        labe5 = tk.Label(self, text="Potential (V)")
        labe5.grid(row=2, column=7, pady = 10)
        
        R2 = tk.Entry(self)       
        R2.grid(row=3, column=8, pady = 10)
        labe6 = tk.Label(self, text="Resistance (Ω)")
        labe6.grid(row=3, column=7, pady = 10)
        
        buttonCalcV = tk.Button(self, text="Calculate V")
        buttonCalcV.grid(row=5, column=3, pady = 10)
        buttonCalcV.config(command=lambda: calc_potential(float(I.get()), float(R1.get())))

        buttonCalcV = tk.Button(self, text="Calculate I")
        buttonCalcV.grid(row=5, column=8, pady = 10)
        buttonCalcV.config(command=lambda: calc_current(float(V.get()), float(R2.get())))                  
        
        bt_button = tk.Button(self, text = 'EXIT', fg = 'red', bg = 'light grey', command = exit)
        bt_button.grid(row=7, column=4, pady = 10)
        button = tk.Button(self, text="Back to Options Menu",
                           command=lambda: controller.show_frame("EM"))
        button.grid(row=7, column=2, pady = 10)

        ansP_text = tk.Label(self, text='')
        ansP_text.grid(row=6, column=2) 
        ansP = tk.Label(self, text='')
        ansP.grid(row=6, column=3)

        ansI_text = tk.Label(self, text='')
        ansI_text.grid(row=6, column=5, columnspan = 2) 
        ansI = tk.Label(self, text='')
        ansI.grid(row=6, column=6, columnspan = 3)
        
        def calc_potential(I, R):
            potential = I*R
            ansP_text.config(text="Potential     = ")
            ansP.config(text = str(potential) + " C")

        def calc_current(V, R):
            current = V / R
            ansI_text.config(text="Current     = ")
            ansI.config(text = str(current) + " A")

class GuassLaw(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        label = tk.Label(self, text="Guass' Law", font=TITLE_FONT)
        label.grid(row=0, column=2, pady = 10)      
        
        label1 = tk.Label(self, text="Force")
        label1.grid(row=1, column=3, pady = 10)
        label2 = tk.Label(self, text="Electric Field")
        label2.grid(row=1, column=7, pady = 10)
        q1 = tk.Entry(self)       
        q1.grid(row=2, column=3, pady = 10)
        labe2 = tk.Label(self, text="Charge 1 (e)")
        labe2.grid(row=2, column=2, pady = 10)
        
        q2 = tk.Entry(self)       
        q2.grid(row=3, column=3, pady = 10)
        labe3 = tk.Label(self, text="Charge 2 (e)")
        labe3.grid(row=3, column=2, pady = 10)
        
        r = tk.Entry(self)       
        r.grid(row=4, column=3, pady = 10)
        labe4 = tk.Label(self, text="Radius (m)")
        labe4.grid(row=4, column=2, pady = 10)
        
        q = tk.Entry(self)       
        q.grid(row=2, column=8, pady = 10)
        labe5 = tk.Label(self, text="Charge (e)")
        labe5.grid(row=2, column=7, pady = 10)
        
        radius = tk.Entry(self)       
        radius.grid(row=3, column=8, pady = 10)
        labe6 = tk.Label(self, text="Radius (m)")
        labe6.grid(row=3, column=7, pady = 10)
        
        buttonCalcF = tk.Button(self, text="Calculate F")
        buttonCalcF.grid(row=5, column=3, pady = 10)
        buttonCalcF.config(command=lambda: calc_coulombs_force(float(q1.get()), float(q2.get()), float(r.get())))
                           
        buttonCalcE = tk.Button(self, text="Calculate E")
        buttonCalcE.grid(row=5, column=8, pady = 10)
        buttonCalcE.config(command=lambda: calc_coulombs_electric(float(q.get()), float(radius.get())))
        
        bt_button = tk.Button(self, text = 'EXIT', fg = 'red', bg = 'light grey', command = exit)
        bt_button.grid(row=7, column=4, pady = 10)
        button = tk.Button(self, text="Back to Options Menu",
                           command=lambda: controller.show_frame("EM"))
        button.grid(row=7, column=2, pady = 10)

        ansF_text = tk.Label(self, text='')
        ansF_text.grid(row=6, column=2) 
        ansF = tk.Label(self, text='')
        ansF.grid(row=6, column=3)

        ansE_text = tk.Label(self, text='')
        ansE_text.grid(row=6, column=5, columnspan = 2) 
        ansE = tk.Label(self, text='')
        ansE.grid(row=6, column=6, columnspan = 3)
        
        def calc_coulombs_force(q1, q2, r):
            e = 1.602177*10**(-19)
            force = (1/(4*math.pi*8.854*10**(-12)))*(q1*e*q2*e/r**2)
            ansF_text.config(text="Force     = ")
            ansF.config(text = str(force) + " N")
        def calc_coulombs_electric(q, radius):
            e = 1.602177*10**(-19)
            force = (1/(4*math.pi*8.854*10**(-12)))*(q*e/radius**2)
            ansE_text.config(text="Electric Field     = ")
            ansE.config(text = str(force) + " N/C")

class LorentzForce(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller        

        
        
        label = tk.Label(self, text="Lorentz Force", font=TITLE_FONT)
        label.grid(row=0, column=2, pady = 10)      
        
        label1 = tk.Label(self, text="Force")
        label1.grid(row=1, column=3, pady = 10)
        
        q = tk.Entry(self)       
        q.grid(row=2, column=3, pady = 10)
        labe2 = tk.Label(self, text="Charge (e)")
        labe2.grid(row=2, column=2, pady = 10)
        
        v = tk.Entry(self)       
        v.grid(row=3, column=3, pady = 10)
        labe3 = tk.Label(self, text="Velocity (m/s^2)")
        labe3.grid(row=3, column=2, pady = 10)
        
        E = tk.Entry(self)       
        E.grid(row=2, column=8, pady = 10)
        labe5 = tk.Label(self, text="Electric Field (E)")
        labe5.grid(row=2, column=7, pady = 10)
        
        B = tk.Entry(self)       
        B.grid(row=3, column=8, pady = 10)
        labe6 = tk.Label(self, text="Magnetic Field (B)")
        labe6.grid(row=3, column=7, pady = 10)
        
        buttonCalcF = tk.Button(self, text="Calculate F")
        buttonCalcF.grid(row=5, column=3, pady = 10)
        buttonCalcF.config(command=lambda: calc_lorentz_force(float(q.get()), float(v.get()), float(E.get()), float(B.get())))
                           
        
        bt_button = tk.Button(self, text = 'EXIT', fg = 'red', bg = 'light grey', command = exit)
        bt_button.grid(row=7, column=4, pady = 10)
        button = tk.Button(self, text="Back to Options Menu",
                           command=lambda: controller.show_frame("EM"))
        button.grid(row=7, column=2, pady = 10)

        ansF_text = tk.Label(self, text='')
        ansF_text.grid(row=6, column=2) 
        ansF = tk.Label(self, text='')
        ansF.grid(row=6, column=3)
        
        def calc_lorentz_force(q, v, E, B):
            e = 1.602177*10**(-19)
            force = q*e*(E + v * B)
            ansF_text.config(text="Force     = ")
            ansF.config(text = str(force) + " N")
        

class Resistivity(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="Resistivity", font=TITLE_FONT)
        label.grid(row=0, column=2, pady = 10)      
        
        label1 = tk.Label(self, text="Force")
        label1.grid(row=1, column=3, pady = 10)
        
        q = tk.Entry(self)       
        q.grid(row=2, column=3, pady = 10)
        labe2 = tk.Label(self, text="Charge (e)")
        labe2.grid(row=2, column=2, pady = 10)
        
        v = tk.Entry(self)       
        v.grid(row=3, column=3, pady = 10)
        labe3 = tk.Label(self, text="Velocity (m/s^2)")
        labe3.grid(row=3, column=2, pady = 10)
        
        E = tk.Entry(self)       
        E.grid(row=2, column=8, pady = 10)
        labe5 = tk.Label(self, text="Electric Field (E)")
        labe5.grid(row=2, column=7, pady = 10)
        
        B = tk.Entry(self)       
        B.grid(row=3, column=8, pady = 10)
        labe6 = tk.Label(self, text="Magnetic Field (B)")
        labe6.grid(row=3, column=7, pady = 10)
        
        buttonCalcF = tk.Button(self, text="Calculate F")
        buttonCalcF.grid(row=5, column=3, pady = 10)
        buttonCalcF.config(command=lambda: calc_lorentz_force(float(q.get()), float(v.get()), float(E.get()), float(B.get())))
                           
        
        bt_button = tk.Button(self, text = 'EXIT', fg = 'red', bg = 'light grey', command = exit)
        bt_button.grid(row=7, column=4, pady = 10)
        button = tk.Button(self, text="Back to Options Menu",
                           command=lambda: controller.show_frame("EM"))
        button.grid(row=7, column=2, pady = 10)

        ansF_text = tk.Label(self, text='')
        ansF_text.grid(row=6, column=2) 
        ansF = tk.Label(self, text='')
        ansF.grid(row=6, column=3)
        
        def calc_lorentz_force(q, v, E, B):
            e = 1.602177*10**(-19)
            force = q*e*(E + v * B)
            ansF_text.config(text="Force     = ")
            ansF.config(text = str(force) + " N")

class Conductivity(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="Conductivity", font=TITLE_FONT)
        label.grid(row=0, column=2, pady = 10)      
        
        label1 = tk.Label(self, text="Force")
        label1.grid(row=1, column=3, pady = 10)
        
        q = tk.Entry(self)       
        q.grid(row=2, column=3, pady = 10)
        labe2 = tk.Label(self, text="Charge (e)")
        labe2.grid(row=2, column=2, pady = 10)
        
        v = tk.Entry(self)       
        v.grid(row=3, column=3, pady = 10)
        labe3 = tk.Label(self, text="Velocity (m/s^2)")
        labe3.grid(row=3, column=2, pady = 10)
        
        E = tk.Entry(self)       
        E.grid(row=2, column=8, pady = 10)
        labe5 = tk.Label(self, text="Electric Field (E)")
        labe5.grid(row=2, column=7, pady = 10)
        
        B = tk.Entry(self)       
        B.grid(row=3, column=8, pady = 10)
        labe6 = tk.Label(self, text="Magnetic Field (B)")
        labe6.grid(row=3, column=7, pady = 10)
        
        buttonCalcF = tk.Button(self, text="Calculate F")
        buttonCalcF.grid(row=5, column=3, pady = 10)
        buttonCalcF.config(command=lambda: calc_lorentz_force(float(q.get()), float(v.get()), float(E.get()), float(B.get())))
                           
        
        bt_button = tk.Button(self, text = 'EXIT', fg = 'red', bg = 'light grey', command = exit)
        bt_button.grid(row=7, column=4, pady = 10)
        button = tk.Button(self, text="Back to Options Menu",
                           command=lambda: controller.show_frame("EM"))
        button.grid(row=7, column=2, pady = 10)

        ansF_text = tk.Label(self, text='')
        ansF_text.grid(row=6, column=2) 
        ansF = tk.Label(self, text='')
        ansF.grid(row=6, column=3)
        
        def calc_lorentz_force(q, v, E, B):
            e = 1.602177*10**(-19)
            force = q*e*(E + v * B)
            ansF_text.config(text="Force     = ")
            ansF.config(text = str(force) + " N")
if __name__ == "__main__": 
    app = PhysSolv()
    app.mainloop()
    

