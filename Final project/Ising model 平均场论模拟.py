# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 12:21:54 2017

@author: 94847
"""
import numpy as np
import matplotlib.pyplot as plt 

T_save=np.array([])
T=0.2
T_step=0.2
s=0
s_save=np.array([])


def f(x,y):
    return x-((1-np.exp(-8*x/y))/(1+np.exp(-8*x/y)))

def fd(x,y):
    return 1-((16*np.exp(-8*x/y))/(T*(1+np.exp(-8*x/y))**2))


while T<8:
    T_save=np.append(T_save,T)
    s=1.1
    while abs(f(s,T))>0.000000001:
        s=s-(f(s,T)/fd(s,T))
    s_save=np.append(s_save,s)
    T=T+T_step

plt.figure()
plt.plot(T_save,s_save)
plt.title("Mean field theory")
plt.ylabel("Magnetization")
plt.xlabel("Temperature")
        
    

