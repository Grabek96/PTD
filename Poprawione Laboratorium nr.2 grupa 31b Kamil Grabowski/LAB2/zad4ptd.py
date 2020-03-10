# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 10:31:08 2019

@author: gk36042
"""

import math as m
import matplotlib.pyplot as p
import numpy.fft as np
import datetime as d
T=1#s6
fs=15000#hz
Na=2
Nb=5
Nc=25
N=T*fs
NN=int(N)
NNN=int(NN/2)
c=[]
b=[]
widm4=[]

for t in range(0,NN-1,1):
    t/=fs
    c.append(t)
    suma=0
    for i in range(1,Nb,1):
       
       suma=(suma+(m.sin(m.sin(m.pi*i/7*t)*m.pi*t*i)/(2*(m.pow(i,2))+1)))
    b.append(suma)


start4=d.datetime.now()   
F= abs(np.rfft(b))
end4=d.datetime.now()

for i in range(0,NNN):
    widm4.append(10*m.log10(F[i]))

p.title('Zad 4 fft')
p.xscale('log')
p.plot(widm4)  
result=('%s')%(end4-start4)
print(result)
p.show()