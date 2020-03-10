# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 10:13:33 2019

@author: gk36042
"""
import math as m
import matplotlib.pyplot as p
import numpy.fft as np
import datetime as d
c1=[]
u=[]
widm=[]
T1=1#2.6 było oryginalnie lecz zbyt długo obliczało dla dft
fs1=8700
N1=T1*fs1
NN1=int(N1)
NN2=int(NN1/2)

for t1 in range(0,NN1-1,1):
    t1/=fs1
    c1.append(t1)
    if t1>=0 and t1<0.15:
        u.append((1/2)*m.pow(abs(m.cos(3*m.pi*t1-m.pi)*m.sin(2.2*m.pi*m.pow(t1,2))),0.32))
         #u.append(1)
    elif t1>=0.15 and t1<0.5:
       # u.append(1.1*t1*(m.cos(10*m.pi*t1-m.pi)/(m.sin(m.pi*m.pow(t1,2)+4))))
        u.append(1.1*t1*((m.cos(10*m.pi*t1-m.pi))/(m.sin(m.pi*m.pow(t1,2))+4)))
    elif t1>=0.5 and t1<1:    
        u.append(((abs((t1+1)*m.pow(m.sin((8*m.pow(t1,2)+m.pi)/(2+0.14)),3)))/8.6))
        # u.append(3)
    elif t1>=1 and t1<1.3:  
        u.append((m.pow(t1,4)*m.log10(t1))/30) 
        # u.append(4)
start=d.datetime.now()
F=abs(np.rfft(u))
end=d.datetime.now()

for i in range(0,NN2):
    widm.append(10*m.log10(F[i]))

p.title('Zad 3 fft ')
p.xscale('log')
p.plot(widm)  

result=('%s')%(end-start)
print(result)
p.show()