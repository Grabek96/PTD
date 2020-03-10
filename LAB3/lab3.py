# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 10:33:41 2020

@author: Grabek96
"""

import math as m
import matplotlib.pyplot as p
import numpy.fft as np

p.figure()

fm=4
fn=8
T=1
Am=1
fs=6200#Hz

mT=[]
zA=[]
zT=[]
Ka=0.5 #24 3 / 0.5
Kp=50# 2/ 50 / 1
N=m.floor(T*fs)
#sygnał informacyjny

for n in range(0,N-1,1):
    
  
    mT.append( Am *m.sin(2 * m.pi * fm * (float(n)/fs)))
    zA.append((Ka * mT[-1] + 1) * m.cos(2 * m.pi * fn * (float(n)/fs) )) #modulacja amplitudy
    zT.append(m.cos(2 * m.pi * fn *(float(n)/fs) + Kp * mT[-1]))   #modulacja kąta
 
    
#p.subplot(2,2,1)   
#p.plot(zT)  
#p.subplot(2,2,2)
#p.plot(zA)  
#p.subplot(2,2,3)
#p.xscale("log") 
#p.plot(zT)

widmo_amp = abs(np.rfft(zT)) 
#f = np.rfftfreq(zA/fs)
#F1==abs(np.fft(zA))
#F2==abs(np.fft(zT))
p.title("WIDMO KP=2")
p.plot(widmo_amp)


#szerokosc pasma
W=max(zA)-min(zA)
W1=max(zT)-min(zT)













p.show()