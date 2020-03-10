# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 21:26:33 2020

@author: Grabek96
"""

import math as m
import matplotlib.pyplot as p
import numpy.fft as np

p.figure()

#zadanie 1
s = 'Hell'
def string2bits(s=''):
    return [bin(ord(x))[2:].zfill(8) for x in s]

Slowo = string2bits(s)
sl=[]
sl=(Slowo[0]+Slowo[1]+Slowo[2]+Slowo[3])
#fn=32#Hz
fs=4000#Hz
T=1#s
A=1
N=m.floor(T*fs)
x1=[]
x=[]
y = []
tab=[]
tabb=[]
tab2=[]
h=[]
odej=[]

GG=len(sl)
bits=int(4000/GG)


N2=2
ograniczone="0100100001"
ogr=len(ograniczone)
#fn=2*m.pow(0.05,-1)
d = 0
sygnal=[]

for n in range(N):
    
    if (n % (N/GG) == 0): #ogr jak 10 bitow
        b = sl[d]        # ograniczone jak 10 bitow
        d = d + 1
               
        if b =="0":
            fn=N2+1/0.03125
            fn1=N2+1/0.03125 
        else:
            fn=N2+2/0.03125
            fn2=N2+2/0.03125
    
    v = m.sin(2.0 * m.pi * fn *(float(n)/fs))
    y.append(v)
    z=m.sin(2.0 * m.pi * fn1 *(float(n)/fs)) #0
    x.append(z)
    z1=m.sin(2.0 * m.pi * 66.0 *(float(n)/fs))
    x1.append(z1)
    o= v*z
    tab.append(o)
    o1=v*z1
    tabb.append(o1)
    o2=o-o1
    odej.append(o2)
    
    
for nn in range(GG):
    mn=0
    for nn2 in range(bits):
        mn=mn+odej[(bits*nn)+nn2]
        tab2.append(mn)
    h.append(mn)
    if h[nn] <0:
        kod=1
    else:
        kod=0
    sygnal.append(kod)    
    
p.subplot(5,1,1)   
p.title("fsk") 
p.plot(y) # sygnał bazowy
p.subplot(5,1,2)
p.plot(tab) # pomnożony sygnał przez 0
p.subplot(5,1,3)
p.plot(tabb) # pomnożony sygnał przez 1
p.subplot(5,1,4)
p.plot(odej)    # odjęty sygnał
p.subplot(5,1,5)
p.plot(tab2)    #sumowanie bitów

print(sygnal)