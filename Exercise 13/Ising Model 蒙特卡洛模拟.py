# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 14:53:07 2017

@author: 94847
"""

import numpy as np
import random 
import matplotlib.pyplot as plt 

T_save=np.array([1.5,2,2.25,4])
def l(x,y=9):
    if x>9:
        x=x-10
    if x<0:
        x=x+y+1
    return x
for k in np.arange(0,4):
    T=T_save[k]
    s=np.ones((10,10))
    t=0
    M=1
    t_save=np.array([])
    M_save=np.array([])
    while t<1000:
        for i in np.arange(0,10):
            for j in np.arange(0,10):
                Ef=2*s[i,j]*(s[l(i+1),j]+s[l(i-1),j]+s[i,l(j+1)]+s[i,l(j-1)])
                if Ef<=0:
                    s[i,j]=-s[i,j]
                if Ef>0:
                    r=random.random()
                    if r<=np.exp(-Ef/T):
                        s[i,j]=-s[i,j]
        
        M=np.sum(s)/100
        t=t+1
        M_save=np.append(M_save,M)
        t_save=np.append(t_save,t)
    fig=plt.figure()
    plt.plot(t_save,M_save,color="black",lw=0.8,label="T=1.5")
    plt.title(r"Ising modle Magnetization vs time")
    plt.xlabel("time")
    plt.ylabel("Magnetization")
    plt.xlim(0,1000)
    plt.ylim(-1,1)
    fig.text(0.35,0.25,"T=%.2f"%T,fontsize=13)

