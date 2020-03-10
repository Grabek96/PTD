# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 22:36:44 2019

@author: gk36042
"""

import math as m
import matplotlib.pyplot as p
p.figure()
f=7#Hz
fs=6200#Hz
T=2.3#s
n=1/T
N=T*fs
NN=int(N)
x=[]
c=[]
y=[]
z=[]
v=[]
g=[]
s=1
#dt=24
#t=double(t)
for t in range(0,NN-1,1):
    t /= fs
    #dt/=10
    c.append(t)
    x.append(m.fabs(m.pow(m.sin(2*m.pi*f*m.pow(t,2)),13))+m.cos(2*m.pi*t))
    #g.append(x)
    #zadanie 2
    y.append(x[-1]*(m.pow(t,3)))
    z.append(1.92*(m.cos(3*m.pi*t/2)+m.cos(m.pow(y[-1],2)/(8*x[-1]+3)*t)))
    v.append((y[-1]*z[-1]/(x[-1]+2))*m.cos(7.2*m.pi*t)+m.sin(m.pi*m.pow(t,2)))
    
    #p.plot(x,'b')
   #m.fabs(m.pow(m.sin*(2*m.pi*f*(m.pow(t,2))),13))+m.cos((2*m.pi)*t)
   #zadanie 3
c1=[]
u=[]
T1=2.6
fs1=8700
N1=T1*fs1
NN1=int(N1)
for t1 in range(0,NN1-1,1):
    t1/=fs
    c1.append(t1)
    if t1>=0 and t1<0.3:
        u.append((1/2)*m.pow(abs(m.cos(3*m.pi*t1)*m.sin(2.2*m.pi*m.pow(t1,2))),0.32))
    elif t1>=0.3 and t1<1:
        u.append(1.1*t1*(m.cos(10*m.pi*t1-m.pi)/(m.sin(m.pi*m.pow(t1,2)+4))))
    elif t1>=1 and t1<2:    
        u.append(((abs((t1+1)*pow(m.sin((8*pow(t1,2)+m.pi)/(2+0.14)),3)))/8.6))
    elif t1>=2 and t1<2.6:  
        u.append((pow(t1,4)*m.log10(t1))/30) 
    
p.subplot(2,2,1)
p.title('Zad 1 ')
p.ylabel('A')
p.plot(c, x)  
p.subplot(2,2,2)
p.title('Zad 2 y(t)' )
p.plot(c, y)
p.subplot(2,2,3)
p.title('Zad 2 z(t)' )
p.plot(c, z)
p.subplot(2,2,4)
p.title('Zad 2 v(t)' )
p.plot(c, v)

  
#print(x)
print(t)
p.show()