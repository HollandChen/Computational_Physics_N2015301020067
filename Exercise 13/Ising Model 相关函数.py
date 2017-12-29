# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 20:48:15 2017

@author: 94847
"""
import numpy as np
import random 
import matplotlib.pyplot as plt 
f=np.zeros((5,10))
T_save=np.array([1.5,2,2.25,3,5])
def l(x,y=19):
    if x>19:
        x=x-20
    if x<0:
        x=x+y+1
    return x
for k in np.arange(0,5):
    T=T_save[k]
    s=np.ones((20,20))
    t=0
    while t<1000:
        for i in np.arange(0,20):
            for j in np.arange(0,20):
                Ef=2*s[i,j]*(s[l(i+1),j]+s[l(i-1),j]+s[i,l(j+1)]+s[i,l(j-1)])
                if Ef<=0:
                    s[i,j]=-s[i,j]
                if Ef>0:
                    r=random.random()
                    if r<=np.exp(-Ef/T):
                        s[i,j]=-s[i,j]
        for i in np.arange(0,20):
            for j in np.arange(0,20):
                for d in np.arange(1,11):
                    f[k,d-1]=f[k,d-1]+s[i,j]*(s[l(i+d),j]+s[l(i-d),j]+s[i,l(j+d)]+s[i,l(j-d)])
        t=t+1
f=f/1600000
fig=plt.figure(figsize=(7,7))
D=np.arange(1,11)
plt.plot(D,f[0,:],c="black",label="T=1.5")
plt.plot(D,f[1,:],c="blue",label="T=2")
plt.plot(D,f[2,:],c="red",label="T=2.25")
plt.plot(D,f[3,:],c="green",label="T=3")
plt.plot(D,f[4,:],c="yellow",label="T=5")
plt.xlim(0,10)
plt.title("Ising model Correlations")
plt.ylabel(r"$f(i)=<s_i s_0>$")
plt.xlabel("i=Distance")
plt.legend()
plt.show()

                
        