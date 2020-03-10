
"""
Created on Wed Jan  8 15:33:41 2020

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
fn=32#Hz
fs=4000#Hz
T=1#s
A=1
N=m.floor(T*fs)

GG=len(sl)

y = []

ograniczone="0100100001"
ogr=len(ograniczone)
fn=2*m.pow(0.1,-1)
d = 0


for n in range(N):
    
    if (n % (N/GG) == 0):
        b = sl[d]
        d = d + 1
               
        if b =="0":
            A = 0.5
        else:
            A = 1
    
    v = A * m.sin(2.0 * m.pi * fn *(float(n)/fs))
    y.append(v)
    
    
p.title("ask") 
#p.plot(y)

F1=abs(np.fft(y))

p.plot(F1)