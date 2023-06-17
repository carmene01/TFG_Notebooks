# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 12:40:47 2023

@author: Carmen
"""

#A --> Ácido acético
#B --> Butanol
#C --> Acetato de butilo
#D --> Agua

import numpy as np
from matplotlib import pyplot 
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import pyplot as plt
from ipywidgets import interact, interactive, fixed, FloatSlider
from ipywidgets import interact, interactive, fixed, IntSlider

#CONDICIONES ESTEQUIOMÉTRICAS
def fun1(Va=125, Vb=375, Vcat=2):
    
    t_final_batch=2500
    dt=60
    #Densidades en g/cm3
    densA=1.049 
    densB=0.8098
    densCAT=1.19
    #Pesos moleculares en g/mol
    PMa=60
    PMb=74
    PMcat=36.46
    PMd=18
    
    Vt=Va+Vb+Vcat
    Na=Va*densA*(1/PMa)
    Nb=Vb*densB*(1/PMb)
    Ncat=Vcat*densCAT*0.37*(1/PMcat)
    Nd=Vcat*densCAT*(1-0.37)*(1/PMd)

    
    Ca=(Na/Vt)*1000
    Cb=(Nb/Vt)*1000
    Ccat=(Ncat/Vt)*1000
    Cc=0
    Cd=(Nd/Vt)*1000
    
    k=(3.18e-3+32.55*Ccat)/3600 #L/mol*s
    #print(k)
    K=2.7
    
    t_array=[]
    Ca_array=[]
    Cb_array=[]
    Cc_array=[]
    Cd_array=[]
    
    t=0

    t_batch=range(0, t_final_batch+dt, dt) 
    
    for y in t_batch:

        Ca_array.append(Ca)
        Cb_array.append(Cb)
        Cc_array.append(Cc)
        Cd_array.append(Cd)
        
        t_array.append(t)

        a=(-k*(Ca*Cb-(Cd*Cc)/K)) 
        b=(-k*(Ca*Cb-(Cd*Cc)/K))
        c=(k*(Ca*Cb-(Cd*Cc)/K))
        d=(k*(Ca*Cb-(Cd*Cc)/K))

        Ca=Ca+dt*a
        Cb=Cb+dt*b
        Cc=Cc+dt*c
        Cd=Cd+dt*d
        
        t=t+dt
    
    plt.figure(figsize=(10,6))
    plt.plot(t_array, Ca_array, 'r-', label="[Ácido acético]")
    plt.plot(t_array, Cb_array, 'g-', label="[Butanol]")
    plt.plot(t_array, Cc_array, 'b-', label="[Acetato de butilo]")
    plt.plot(t_array, Cd_array, 'y-', label="[Agua]")
    
    plt.legend(fontsize=14)
    plt.xlim(0,2500)
    plt.ylim(0)
    plt.xlabel("Tiempo (s)", fontsize=16)
    plt.ylabel("Concentración (mol/L)", fontsize=16)
    plt.xticks(fontsize = 14)
    plt.yticks(fontsize = 14)
    plt.show() 
    
w=interactive(fun1, {'manual':True}, Va=IntSlider(min=120, max=125, value=125, description='$Va$'), Vb=IntSlider(min=375, max=400, value=375, description='$Vb$'), Vcat=IntSlider(min=1, max=3, value=2, description='$Vcat$'))