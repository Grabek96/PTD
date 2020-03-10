# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 22:36:44 2019

@author: gk36042 lab2
"""

import math as m
import matplotlib.pyplot as p
import lab1
#import zad3ptd  #3 zadanie
#import zad4ptd  #4 zadanie
import datetime as d
 
def dft(s):
     
    N1 = len(s)
    N11=int(N1/2)
    fs=6200
    rzeczywista = []
    urojona = []
    widmo1=[]
    fk=[]
    widmo2=[] 
    for k in range(N11-1): 
        aa = 0.0
        bb = 0.0
        for n in range(N1):
            
            ei = (2 * m.pi * k * n)/N1
            aa += s[n] * m.sin(ei)
            bb += s[n] * m.cos(ei)
             
        rzeczywista.append(aa)
        urojona.append(bb)

        widmo=(m.sqrt(m.pow(rzeczywista[k],2) + m.pow(urojona[k],2)))
        widmo1.append(widmo)
        
        skala=10*m.log10(widmo)
        widmo2.append(skala)
        fk.append(k*fs/N1)
        
        
    return widmo2

          
    
    

   #ZADANIE 1 i 2
p.subplot(2,2,1)
p.xscale('log')
start=d.datetime.now() 
p.plot(dft(lab1.x))
end=d.datetime.now() 

p.subplot(2,2,2)
p.xscale('log')
start1=d.datetime.now() 
p.plot(dft(lab1.y))
end1=d.datetime.now()

p.subplot(2,2,3)
p.xscale('log')
start2=d.datetime.now() 
p.plot(dft(lab1.z))
end2=d.datetime.now()

p.subplot(2,2,4)
p.xscale('log')
start3=d.datetime.now()
p.plot(dft(lab1.v))
end3=d.datetime.now()


'''
 #ZADANIE 3
p.title('Zad 3 ')
p.xscale('log')
start=d.datetime.now()
p.plot(dft(zad3ptd.u))
end=d.datetime.now()
'''
'''
#ZADANIE 4
p.xscale('log')
start=d.datetime.now()
p.plot(dft(zad4ptd.b))
end=d.datetime.now()


'''




# Jesli jest 3 badz 4 zadanie to nalezy zakomentować od 96-102 lini bo nie ma wtedy pomiarów i mogą wyskoczyć błędy
result=('%s')%(end-start)
print(result)
result1=('%s')%(end1-start1)
print(result1)
result2=('%s')%(end2-start2)
print(result2)
result3=('%s')%(end3-start3)
print(result3)

p.show()