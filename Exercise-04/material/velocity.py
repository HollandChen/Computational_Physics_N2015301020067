import numpy as np
import pylab as pl
step=0.05
g=9.8
time=[]
velocity=[]
t_end=10
N=t_end/step
n=0
t=0
v=0
while n<=N:
    time.append(t)
    velocity.append(v)
    v=v-g*step
    t=t+step
    n=n+1
def plot_01():
    x=time
    y=velocity
    pl.plot(x,y,'b')
    pl.title('velocity of a freely falling object') 
    pl.xlabel('time/s')
    pl.ylabel('velocity/m/s')
    pl.xlim(0.0,10.0)
    pl.ylim(-100.0,0.0)
    pl.show()
plot_01()

