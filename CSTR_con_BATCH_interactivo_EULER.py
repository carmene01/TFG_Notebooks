# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#Librerías
import numpy as np 
import matplotlib.pyplot as plt
from ipywidgets import interact, interactive, fixed, FloatSlider
from ipywidgets import interact, interactive, fixed, IntSlider


def cstr_batch(t_reg_estacionario=5400, t_final_batch=5400, T=294, Ua0=0.000605, Ub0=0.000713, Vreactor=1.45, Ca0_t=0.1, Cb0_t=0.1, dt=60):
    
    k=1.22*(10**8)*np.exp(-6196.6/T)
    U0=Ua0+Ub0
    τ=Vreactor/U0
    Ca0=Ca0_t*(Ua0/U0)
    Cb0=Cb0_t*(Ub0/U0)
    
    t_array=[]
    Ca_array=[]
    Cb_array=[]
    Cc_array=[]
    Cd_array=[]
    
    Ca=0
    Cb=0
    Cc=0
    Cd=0
    t=0
    
    #Tiempo desde puesta en marcha del reactor CSTR hasta alcanzar el regimen estacionario
    t_arranque=range(0, t_reg_estacionario, dt) 
    
    #Tiempo final operación reactor batch
    t_final=t_reg_estacionario+t_final_batch 
    
    #Tiempo desde que se pone en marcha el batch hasta final operación
    t_batch=range(t_reg_estacionario, t_final, dt)
    
    #Antes bucle arranque
    estacionario=False
    Ca_anterior=100 
    
    for n in t_arranque: 
        
        Ca_array.append(Ca)
        Cb_array.append(Cb)
        Cc_array.append(Cc)
        Cd_array.append(Cd)
        
        t_array.append(t)

        a=(Ca0-Ca)/τ-k*Ca*Cb
        b=(Cb0-Cb)/τ-k*Ca*Cb
        c=-Cc/τ+k*Ca*Cb
        d=-Cd/τ+k*Ca*Cb

        Ca=Ca+dt*a
        Cb=Cb+dt*b
        Cc=Cc+dt*c
        Cd=Cd+dt*d
        
        if not estacionario: 
            if((abs((Ca-Ca_anterior)/Ca))<1e-4):
                estacionario=True
                t_estacionario=t
            Ca_anterior=Ca
        
        t=t+dt
    
    for y in t_batch:

        Ca_array.append(Ca)
        Cb_array.append(Cb)
        Cc_array.append(Cc)
        Cd_array.append(Cd)
        
        t_array.append(t)

        a=-k*Ca*Cb
        b=-k*Ca*Cb
        c=k*Ca*Cb
        d=k*Ca*Cb

        Ca=Ca+dt*a
        Cb=Cb+dt*b
        Cc=Cc+dt*c
        Cd=Cd+dt*d
        
        t=t+dt
    
    plt.figure(figsize=(10,6))
    plt.plot(t_array, Ca_array,'r-',label="Ca")
    plt.plot(t_array, Cb_array,'b-',label="Cb")
    plt.plot(t_array, Cc_array, 'g-',label="Cc")
    plt.plot(t_array, Cd_array, 'y-',label="Cd")
    
    plt.legend(fontsize=14)
    plt.xlim(-500,11000)
    plt.ylim(-0.005, 0.055)
    plt.xlabel("Tiempo", fontsize=16)
    plt.ylabel("Concentración", fontsize=16)
    plt.xticks(fontsize = 14)
    plt.yticks(fontsize = 14)
    
    if estacionario:
        t_array_2=[t_estacionario, t_estacionario]
        y=[0, 0.05]
        plt.plot(t_array_2, y)

w=interactive(cstr_batch, {'manual':True}, t_reg_estacionario=IntSlider(min=1, max=5400, value=5400, step=60, description='$t_{r.estac}$'),  t_final_batch=IntSlider(min=1, max=5400, value=5400, step=60, description='$t_{batch}$'), T=IntSlider(min=273, max=300, value=294, description='$Temp.$'), Ua0=FloatSlider(min=1E-4, max=1E-3, value=0.000605, step=0.0001, description='$U_{a0}$', readout_format='.4f'), Ub0=FloatSlider(min=1E-4, max=0.001, value=0.000713, step=0.0001,  description='$U_{b0}$', readout_format='.4f'), Vreactor=FloatSlider(min=1, max=20, value=1.45, description='$V_{reactor}$'), Ca0_t=FloatSlider(min=0, max=1, value=0.1, description='$C_{a0}$', step=0.01), Cb0_t=FloatSlider(min=0, max=1, value=0.1,  description='$C_{b0}$', step=0.01), dt=IntSlider(min=1, max=100, value=60, description='$Δt$'))

