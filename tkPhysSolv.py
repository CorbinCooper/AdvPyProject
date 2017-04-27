# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 16:14:04 2017
@author: Robert Millican, Eric Hartline, Corbin Cooper
"""

import tkinter as tk   # python3
#import Tkinter as tk   # python
from math import sqrt

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
       
        lbl_new = tk.Label(self, width = 35, text = "Newton's laws of motion are\nthree physical laws that describe\nthe relationship between a body and\nthe forces acting upon it, and its\nm.otion in response to those forces.")
        lbl_new.grid(row=1,column=1, padx = 5)
        
        lbl_em = tk.Label(self, width = 35, text = "Electromagnetism is a branch of\nphysics involving the study\nof the electromagnetic \nforce, a type of physical\ninteraction that occurs between\nelectrically charged particles.")
        lbl_em.grid(row=1,column=2, padx = 5)

        button1.grid(row=2, column=0, padx = 5, pady = 5)
        button2.grid(row=2, column=1, padx = 5)
        button3.grid(row=2, column=2, padx = 5)
        
        bt_button = tk.Button(self, text = 'EXIT', fg = 'red', bg = 'light grey', command = exit)
        bt_button.grid(row=3, column=1, pady = 10)        
        
#        bt_kine = tk.Button(self, border = '3', text="Kinematics",
#                            command=lambda: controller.show_frame("Kinematics"))
#        bt_kine.grid(row=4,column=0)
class oneDmotion(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="One-Dimensional Motion", font=TITLE_FONT)
        label.grid(row=0,  column=1, pady=10)
        
        lb_kine = tk.Label(self, font=SUB_FONT, text='Kinematics')
        lb_mom = tk.Label(self, font=SUB_FONT, text='Momentum')
        lb_ff = tk.Label(self, font=SUB_FONT, text='Free Fall')
        lb_kine.grid(row=1,column=0)
        lb_mom.grid(row=1,column=1)
        lb_ff.grid(row=1,column=2)        
        
        lb_kineD = tk.Label(self, text = 'Kinematics is the study of motion\nusing mathematics. One-dimensional\nkinematics with constant \nacceleration utilizes equations\nthat relate position, velocity and\nacceleration at two instances in\ntime.', width=35)
        lb_momD = tk.Label(self, width=35, text = 'Momentum is the mass of an object\nmultiplied by its velocity.\nConservation of momentum is used\nwhen acceleration is not constant\nand energy is not conserved.')
        lb_ffD = tk.Label(self, width=35, text = 'Free fall is a subsection of\nkinematics in which an object is\ndropped or thrown vertically near a\nplanets surface and accelerates\nonly due to the influence of\ngravity on the object.')      
        lb_kineD.grid(row=2,column=0)        
        lb_momD.grid(row=2,column=1)        
        lb_ffD.grid(row=2,column=2)        
        
        bt_kine = tk.Button(self, border = '3', text="Kinematics",
                            command=lambda: controller.show_frame("Kinematics"))
        bt_mom = tk.Button(self, border = '3', text='Momentum',
                           command=lambda: controller.show_frame("Momentum"))
        bt_ff = tk.Button(self, border = '3', text='Free Fall',
                           command=lambda: controller.show_frame("FreeFall"))
        bt_kine.grid(row=3,column=0)
        bt_mom.grid(row=3,column=1)
        bt_ff.grid(row=3,column=2)        
                
        button = tk.Button(self, border = '3', text="Back to the home page",
                           command=lambda: controller.show_frame("StartPage"))
        button.grid(row=5,column=0)
    
        bt_button = tk.Button(self, text = 'EXIT', fg = 'red', bg = 'light grey', command = exit)
        bt_button.grid(row=5,column=2)
        
class Kinematics(tk.Frame):

        
#    def Calculate (si,sf,vi,vf,a,t):
#        CheckFilled(si,sf,vi,vf,a,t)
        
    def __init__(self, parent, controller):
        def isFloat(string):
            try:
                float(string)
                return True
            except ValueError:
                return False     
                
        def CheckFilled(si,sf,vi,vf,a,t,siHave,sfHave,viHave,vfHave,aHave,tHave):
            lb_val_calc_si.config(text='')
            lb_val_calc_sf.config(text='')
            lb_val_calc_vi.config(text='')
            lb_val_calc_vf.config(text='')
            lb_val_calc_a.config(text='')
            lb_val_calc_t.config(text='')
                        
            if siHave:
                lb_val_calc_si.config(text = si)
            if sfHave:
                lb_val_calc_sf.config(text = sf)
            if viHave:
                lb_val_calc_vi.config(text = vi)
            if vfHave:
                lb_val_calc_vf.config(text = vf)
            if aHave:
                lb_val_calc_a.config(text = a)
            if tHave:
                lb_val_calc_t.config(text = t)
            return;
          
        #vf = vi + a*t  
        def eqnOne(vi,vf,a,t,viHave,vfHave,aHave,tHave):
            if(viHave):
                vi=float(vi)
            if(vfHave):
                vf=float(vf)
            if(aHave):
                a=float(a)
            if(tHave):
                t=float(t)
            
            if(viHave and aHave and tHave):
                calcVf = vi + a*t
                lb_val_calc_vf.config(text = calcVf)
            if(vfHave and aHave and tHave):
                calcVi = a*t - vf
                lb_val_calc_vi.config(text = calcVi)
            if(viHave and vfHave and tHave):
                calcA = (vf - vi) / t
                lb_val_calc_a.config(text = calcA)
            if(viHave and vfHave and aHave):
                calcT = (vf - vi) / a
                lb_val_calc_t.config(text = calcT)
            return;
            
            if(isFloat(vi)):
                viHave=True
            if(isFloat(vf)):
                vfHave=True
            if(isFloat(a)):
                aHave=True
            if(isFloat(t)):
                tHave=True
        
        #sf = si + vi*t + 0.5*a*t^2
        def eqn2(si,sf,vi,a,t,siHave,sfHave,viHave,aHave,tHave):
            if(siHave):
                si=float(si)
            if(sfHave):
                sf=float(sf)
            if(viHave):
                vi=float(vi)
            if(aHave):
                a=float(a)
            if(tHave):
                t=float(t)
            
            if(siHave and viHave and aHave and tHave):
                calcSf = si + vi*t + 0.5*a*t**2
                lb_val_calc_sf.config(text = calcSf)
            if(sfHave and viHave and aHave and tHave):
                calcSi = -sf + vi*t + 0.5*a*t**2
                lb_val_calc_si.config(text = calcSi)
            if(siHave and sfHave and aHave and tHave):
                calcVi = (sf - si - 0.5*a*t**2)/t
                lb_val_calc_vi.config(text = calcVi)
            if(siHave and sfHave and viHave and tHave):
                calcA = (sf - si - vi*t)/(0.5*t**2)
                lb_val_calc_a.config(text = calcA)
            if(siHave and sfHave and viHave and aHave):
                ds = sf - si
                if((vi**2 - 4*0.5*a*(-ds)) >0):
                    calcT1 = (-vi + sqrt(vi**2 - 4*0.5*a*(-ds)))/(2*0.5*a)
                    calcT2 = (-vi - sqrt(vi**2 - 4*0.5*a*(-ds)))/(2*0.5*a)
                else:
                    print("discriminate not real")
                if(calcT1 > 0):
                    lb_val_calc_t.config(text = calcT1)
                elif(calcT2 >0):
                    lb_val_calc_t.config(text = calcT2)
                else:
                    print("No positive time")
            
            if(isFloat(si)):
                siHave=True
            if(isFloat(sf)):
                sfHave=True
            if(isFloat(vi)):
                viHave=True
            if(isFloat(a)):
                aHave=True
            if(isFloat(t)):
                tHave=True

                   
            return;
        def Calculate(si,sf,vi,vf,a,t):
            siHave = isFloat(si)            
            sfHave = isFloat(sf)
            viHave = isFloat(vi)
            vfHave = isFloat(vf)
            aHave = isFloat(a)
            tHave = isFloat(t)

            CheckFilled(si,sf,vi,vf,a,t,siHave,sfHave,viHave,vfHave,aHave,tHave)
            
#            if (not(viHave and vfHave and aHave and tHave)):
            eqnOne(vi,vf,a,t,viHave,vfHave,aHave,tHave)

#            if(not(siHave and sfHave and viHave and aHave and tHave)):
            eqn2(si,sf,vi,a,t,siHave,sfHave,viHave,aHave,tHave)
 
#            if (not(viHave and vfHave and aHave and tHave)):
            eqnOne(vi,vf,a,t,viHave,vfHave,aHave,tHave)
           
            return;

        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="Kinematics", font=TITLE_FONT)
        label.grid(row=0, column=0, columnspan = 5, pady=10)
        
        lb_intVal = tk.Label(self, text="Please enter all known values below:")        
        lb_intVal.grid(row=1,column=0)        
        
        lb_aT = tk.Label(self, text="Acceleration")
        lb_tT = tk.Label(self, text="Time")
        lb_aT.grid(row=2, column=1, columnspan = 2)
        lb_tT.grid(row=2, column=3, columnspan=2)
        
        lb_a = tk.Label(self, text="a (m/s^2) = ", padx=2)
        en_a = tk.Entry(self, text="*", width=10)
        lb_t = tk.Label(self, text="     t (s) = ")
        en_t = tk.Entry(self, width=10)
        lb_a.grid(row=3, column=1)
        en_a.grid(row=3, column=2)
        lb_t.grid(row=3, column=3)
        en_t.grid(row=3, column=4)
        

        lb_type = tk.Label(self, text="Type", pady = 5)
        lb_initial = tk.Label(self, text="Initial")
        lb_final = tk.Label(self, text="Final")
        lb_type.grid(row=4, column=0)        
        lb_initial.grid(row=4, column=1, columnspan = 2)
        lb_final.grid(row=4, column=3, columnspan=2)

        lb_pos = tk.Label(self, text="Position")
        lb_si = tk.Label(self, text="si (m) = ")  
        en_si = tk.Entry(self, width=10)
        lb_sf = tk.Label(self, text="sf (m) = ")        
        en_sf = tk.Entry(self, width=10)
        lb_pos.grid(row=5, column=0)
        lb_si.grid(row=5, column=1)  
        en_si.grid(row=5, column=2)
        lb_sf.grid(row=5, column=3)        
        en_sf.grid(row=5, column=4)

        lb_vel = tk.Label(self, text="Velocity")
        lb_vi = tk.Label(self, text="vi (m/s) = ")  
        en_vi = tk.Entry(self, width=10)
        lb_vf = tk.Label(self, text="vf (m/s) = ")        
        en_vf = tk.Entry(self, width=10)
        lb_vel.grid(row=6, column=0)
        lb_vi.grid(row=6, column=1)  
        en_vi.grid(row=6, column=2)
        lb_vf.grid(row=6, column=3)        
        en_vf.grid(row=6, column=4)
        
        lb_calcVal = tk.Label(self, text="Click on CALCULATE and values will display below:")        
        bt_calc = tk.Button(self, text="CALCULATE",
                            command=lambda: Calculate(en_si.get(),en_sf.get(),en_vi.get(),en_vf.get(),en_a.get(),en_t.get()))
        lb_calcVal.grid(row=7,column=0,columnspan=3)        
        bt_calc.grid(row=7,column=4, pady=10)
        
        lb_calc_a = tk.Label(self, text="a (m/s^2) = ", padx=2)
        lb_val_calc_a = tk.Label(self, width=10)
        lb_calc_t = tk.Label(self, text="     t (s) = ")
        lb_val_calc_t = tk.Label(self, width=10)
        lb_calc_a.grid(row=8, column=1)
        lb_val_calc_a.grid(row=8, column=2)
        lb_calc_t.grid(row=8, column=3)
        lb_val_calc_t.grid(row=8, column=4)
        

        lb_calc_type = tk.Label(self, text="Type", pady = 5)
        lb_calc_initial = tk.Label(self, text="Initial")
        lb_calc_final = tk.Label(self, text="Final")
        lb_calc_type.grid(row=9, column=0)        
        lb_calc_initial.grid(row=9, column=1, columnspan = 2)
        lb_calc_final.grid(row=9, column=3, columnspan=2)

        lb_calc_pos = tk.Label(self, text="Position")
        lb_calc_si = tk.Label(self, text="si (m) = ")  
        lb_val_calc_si = tk.Label(self, width=10)
        lb_calc_sf = tk.Label(self, text="sf (m) = ")        
        lb_val_calc_sf = tk.Label(self, width=10)
        lb_calc_pos.grid(row=10, column=0)
        lb_calc_si.grid(row=10, column=1)  
        lb_val_calc_si.grid(row=10, column=2)
        lb_calc_sf.grid(row=10, column=3)        
        lb_val_calc_sf.grid(row=10, column=4)

        lb_calc_vel = tk.Label(self, text="Velocity")
        lb_calc_vi = tk.Label(self, text="vi (m/s) = ")  
        lb_val_calc_vi = tk.Label(self, width=10)
        lb_calc_vf = tk.Label(self, text="vf (m/s) = ")        
        lb_val_calc_vf = tk.Label(self, width=10)
        lb_calc_vel.grid(row=11, column=0)
        lb_calc_vi.grid(row=11, column=1)  
        lb_val_calc_vi.grid(row=11, column=2)
        lb_calc_vf.grid(row=11, column=3)        
        lb_val_calc_vf.grid(row=11, column=4)
    
    
        button = tk.Button(self, border = '3', text="Back to the home page",
                           command=lambda: controller.show_frame("StartPage"))
        button.grid(row=15, column=0, pady=10)
        
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
#        Ftype.set("Generic")
        
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

            label1 = tk.Label(self)
            label2 = tk.Label(self)
            
            label1.grid(row=6, column=3, sticky='e')
            label2.grid(row=7, column=3, sticky='e')        
       
            if Ftype.get() == "Generic":
                if find.get() == "Force":
                    label1.config(text="               Mass (kg): ")
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
                elif find.get() == "Acceleration":
                    label1.config(text="Force (N): ")
                    force = tk.Entry(self)
                    force.grid(row=6, column=4)
                    label2.config(text="                       Mass (kg):")
                    mass = tk.Entry(self)
                    mass.grid(row=7, column=4)
                else:
                    print('')

            if Ftype.get() == "Gravity":
                if find.get() == "Weight":
                    label1.config(text="                   Mass (kg): ")
                    mass = tk.Entry(self)
                    mass.grid(row=6, column=4)
                    label2.config(text="       Gravity (m/s^2): ")
                    grav = tk.Entry(self)
                    grav.grid(row=7, column=4)
                elif find.get() == "Mass":
                    label1.config(text="Weight (N): ")
                    weight = tk.Entry(self)
                    weight.grid(row=6, column=4)
                    label2.config(text="       Gravity (m/s^2): ")
                    grav = tk.Entry(self)
                    grav.grid(row=7, column=4)
                elif find.get() == "Gravity":
                    label1.config(text="Weight (N): ")
                    weight = tk.Entry(self)
                    weight.grid(row=6, column=4)
                    label2.config(text="                       Mass (kg):")
                    mass = tk.Entry(self)
                    mass.grid(row=7, column=4)
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
                elif find.get() == "Spring Constant":
                    label1.config(text="Spring Force (N): ")
                    force = tk.Entry(self)
                    force.grid(row=6, column=4)
                    label2.config(text="Displacement (m): ")
                    disp = tk.Entry(self)
                    disp.grid(row=7, column=4)
                elif find.get() == "Displacement":
                    label1.config(text="Spring Force (N): ")
                    force = tk.Entry(self)
                    force.grid(row=6, column=4)
                    label2.config(text="       Spring Constant:")
                    cons = tk.Entry(self)
                    cons.grid(row=7, column=4)
                else:
                    print('')

            if Ftype.get() == "Friction":
                if find.get() == "Friction Force":
                    label1.config(text="     Friction Coefficient: ")
                    coeff = tk.Entry(self)
                    coeff.grid(row=6, column=4)
                    label2.config(text="     Normal Force (N): ")
                    norm = tk.Entry(self)
                    norm.grid(row=7, column=4)
                elif find.get() == "Friction Coefficient":
                    label1.config(text="     Friction Force (N): ")
                    force = tk.Entry(self)
                    force.grid(row=6, column=4)
                    label2.config(text="     Normal Force (N): ")
                    norm = tk.Entry(self)
                    norm.grid(row=7, column=4)
                elif find.get() == "Normal Force":
                    label1.config(text="     Friction Force (N): ")
                    force = tk.Entry(self)
                    force.grid(row=6, column=4)
                    label2.config(text="    Friction Coefficient:")
                    coeff = tk.Entry(self)
                    coeff.grid(row=7, column=4)
                else:
                    print('')

            if Ftype.get() == "Pressure":
                if find.get() == "Force":
                    label1.config(text="     Pressure (Pa): ")
                    press = tk.Entry(self)
                    press.grid(row=6, column=4)
                    label2.config(text="     Area (m^2): ")
                    area = tk.Entry(self)
                    area.grid(row=7, column=4)
                elif find.get() == "Pressure":
                    label1.config(text="          Force (N): ")
                    force = tk.Entry(self)
                    force.grid(row=6, column=4)
                    label2.config(text="            Area (m^2): ")
                    area = tk.Entry(self)
                    area.grid(row=7, column=4)
                elif find.get() == "Area":
                    label1.config(text="     Force (N): ")
                    force = tk.Entry(self)
                    force.grid(row=6, column=4)
                    label2.config(text="    Pressure (Pa):")
                    press = tk.Entry(self)
                    press.grid(row=7, column=4)
                else:
                    print('')

            else:
                print('')

        def Gen_Force(mass, accel):
            force = mass * accel
            lbl_Atype.config(text="Force = ")
            lbl_ans.config(text = str(force) + " N")

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
                           command=lambda: tk.Print(4))
        buttonCalcF.grid(row=5, column=3, pady = 10)
        buttonCalcE = tk.Button(self, text="Calculate E",
                           command=lambda: tk.Print(4))
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
                           command=lambda: tk.Print(4))
        buttonCalcF.grid(row=5, column=3, pady = 10)
        buttonCalcE = tk.Button(self, text="Calculate I",
                           command=lambda: tk.Print(4))
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
    
