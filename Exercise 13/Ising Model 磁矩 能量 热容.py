# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 14:32:31 2017

@author: 94847
"""

import numpy as np 
import matplotlib.pyplot as plt 
import random
M_save=np.array([])
E_save=np.array([])
c_save=np.array([])
T_save=np.array([])
"""温度序列"""
a=np.arange(1,5.2,0.2)
a=np.insert(a,6,2.1)
a=np.insert(a,8,2.3)
"""定义周期性边界条件"""
def l(x,y=9):
    if x>9:
        x=x-10
    if x<0:
        x=x+y+1
    return x
for k in a:
    T=k
    H=0
    s=np.ones((10,10))
    t=0
    m=1
    m_save=np.array([])
    e_save=np.array([])
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
        m=np.sum(s)/100
        t=t+1
        m_save=np.append(m_save,m)
        e=0
        for i in np.arange(0,9):
            for j in np.arange(0,9):
                e=e-s[i,j]*(s[l(i+1),j]+s[l(i-1),j]+s[i,l(j+1)]+s[i,l(j-1)])
        e=e/200
        e_save=np.append(e_save,e)
    M_save=np.append(M_save,np.sum(m_save)/1000)
    E_save=np.append(E_save,np.sum(e_save)/1000)
    c_save=np.append(c_save,((np.sum(e_save**2)/1000)-(np.sum(e_save)/1000)**2)/(T**2))
    T_save=np.append(T_save,T)
fig1=plt.figure(figsize=(7,7))
plt.scatter(T_save,M_save,c="red",label="$<s>$")
plt.xlabel("Temperature")
plt.ylabel(" spin ")
plt.title(r"$<s> vs T$")
fig2=plt.figure(figsize=(6,6))
plt.scatter(T_save,E_save,c="blue",label="E")
plt.title(r"$E vs T$")
plt.xlabel("Temperature")
plt.ylabel("Energy per spin ")
fig3=plt.figure(figsize=(6,6))
plt.scatter(T_save,c_save,c="black",label="c")
plt.title(r"$C vs T$")
plt.xlabel("Temperature")
plt.ylabel("Specific heat per spin ")
plt.show()
