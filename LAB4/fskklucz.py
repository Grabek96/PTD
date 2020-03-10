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

GG=len(sl)

y = []
N2=2
ograniczone="0100100001"
ogr=len(ograniczone)
#fn=2*m.pow(0.05,-1)
d = 0


for n in range(N):
    
    if (n % (N/GG) == 0): #ogr jak 10 bitow
        b = sl[d]        # ograniczone jak 10 bitow
        d = d + 1
               
        if b =="0":
           fn=N2+1/0.1 
        else:
            fn=N2+2/0.1
    
    v = m.sin(2.0 * m.pi * fn *(float(n)/fs))
    y.append(v)
    
    
p.title("Fsk") 
p.plot(y)
F1=abs(np.fft(y))
p.plot(F1)