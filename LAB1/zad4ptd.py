# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 10:31:08 2019

@author: gk36042
"""

import math as m
import matplotlib.pyplot as p

T=6#s
fs=15000#hz
Na=2#Na=2 lecz pętla sumująca się wtedy nie wykona 
Nb=5
Nc=25
N=T*fs
NN=int(N)
c=[]
b=[]


for t in range(0,N-1,1):
    t/=fs
    c.append(t)
    suma=0
    for i in range(1,Nc-1,1):#dla Na+1
       # b.append(m.sin(m.sin(m.pi*i/7*t)*m.pi*t*i)/(2*m.pow(i,2)+1))
       suma=(suma+(m.sin(m.sin(m.pi*i/7*t)*m.pi*t*i)/(2*(m.pow(i,2))+1)))
    b.append(suma)




p.title('Zad 4 N=25')
p.ylabel('A')
p.plot(c,b)  
p.show()