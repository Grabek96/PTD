# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 23:08:40 2019

@author: gk36042
"""

import math as m
import matplotlib.pyplot as p
import numpy.fft as np
import datetime as d
import numpy as nu
p.figure()
f=7#Hz
fs=6200#Hz
T=1#s 2.6 było oryginalnie lecz zbyt długo obliczało dla dft
n=1/T
N=T*fs
NN=int(N)
N2=int(N)
N3=int(N2/2)
N4=N3


x=[]
c=[]
y=[]
z=[]
v=[]
CC=[]
F=[]
widm=[]
widm1=[]
widm2=[]
widm3=[]
s=1
i=0
#widmo1=[]
for t in range(0,NN-1,1):
    t /= fs
  
    c.append(t)
    x.append(m.fabs(m.pow(m.sin(2*m.pi*f*m.pow(t,2)),13))+m.cos(2*m.pi*t))
   
    #zadanie 2
    y.append(x[-1]*(m.pow(t,3)))
    z.append(1.92*(m.cos(3*m.pi*t/2)+m.cos(m.pow(y[-1],2)/(8*x[-1]+3)*t)))
    v.append((y[-1]*z[-1]/(x[-1]+2))*m.cos(7.2*m.pi*t)+m.sin(m.pi*m.pow(t,2)))
    
    
#

    #czasy

start=d.datetime.now()   
F = abs(np.rfft(x))
end=d.datetime.now()

start1=d.datetime.now()
F1 = abs(np.rfft(y))
end1=d.datetime.now()

start2=d.datetime.now()
F2 = abs(np.rfft(z))
end2=d.datetime.now()

start3=d.datetime.now()
F3 = abs(np.rfft(v))

end3=d.datetime.now()

for i in range(0,N4):
    
    widm.append(10*m.log10(F[i]))
    widm1.append(10*m.log10(F1[i]))
    widm2.append(10*m.log10(F2[i]))
    widm3.append(10*m.log10(F3[i]))
    
p.subplot(2,2,1)
p.title('fft dla x')
p.xscale('log')
p.plot(widm)
p.subplot(2,2,2)
p.xscale('log')
p.title('fft dla y')
p.plot(widm1)
p.subplot(2,2,3)
p.xscale('log')
p.title('fft dla z')
p.plot(widm2)
p.subplot(2,2,4)
p.xscale('log')
p.title('fft dla v')
p.plot(widm3)
 
result=('%s')%(end-start)
print(result)
result1=('%s')%(end1-start1)
print(result)
result2=('%s')%(end2-start2)
print(result)
result3=('%s')%(end3-start3)
print(result)


p.show()