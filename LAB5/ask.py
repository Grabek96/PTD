
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
x=[]
tab=[]
tabb=[]
h=[]
ograniczone="0100100001"
ogr=len(ograniczone)
fn=2*m.pow(0.03125,-1)#0.1 dla 10 bitów
d = 0
bit=(T/GG)
bits=int(4000/GG)
sygnal=[]

for n in range(N):
    
    if (n % (N/GG) == 0):
        b = sl[d]
        d = d + 1
               
        if b =="0":
            A = 1
        else:
            A = 2
    
    v = A * m.sin(2.0 * m.pi * fn *(float(n)/fs))
    y.append(v)
    z=m.sin(2.0 * m.pi * fn *(float(n)/fs))
    x.append(z)
    o= v*z
    tab.append(o)
    

for nn in range(GG):
    mn=0
    for nn2 in range(bits):
        mn=mn+tab[(bits*nn)+nn2]
        tabb.append(mn)
    h.append(mn)
    if h[nn] >100:
        kod=1
    else:
        kod=0
    sygnal.append(kod)
    
    
    
    
p.subplot(4,1,1)   
p.title("ask") 
p.plot(y)
p.subplot(4,1,2)
p.plot(x)
p.subplot(4,1,3)
p.plot(tab)
p.subplot(4,1,4)
p.plot(tabb)
print(sygnal)

#F1=abs(np.rfft(y))

#p.plot(F1)