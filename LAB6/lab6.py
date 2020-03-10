# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 15:27:27 2020

@author: Grabek96
"""
import math as m

sl=[1,0,1,1] #slowo
x7=sl[0]
x6=sl[1]
x5=sl[2]
x3=sl[3]

x4=x5^x6^x7     #poprawna 0
x2=1#x3^x6^x7   #poprawna 0
x1=0#x3^x5^x7     #poprawna 1

#Poprawne wartosci dla porownania 
xp1=x3^x5^x7 
xp4=x5^x6^x7   
xp2=x3^x6^x7 
xp7=sl[0]
xp6=sl[1]
xp5=sl[2]
xp3=sl[3]

sl2=[x7,x6,x5,x4,x3,x2,x1]

#odwrotnie wpisane do listy parametry
sl3=[x1,x2,x3,x4,x5,x6,x7]

# poprawna lista dla porownania
poprawna=[xp1,xp2,xp3,xp4,xp5,xp6,xp7]

i=0
flaga=0


for i in range(2):
  c=sl
  x1prim=x3^x5^x7
  x2prim=x3^x6^x7
  x4prim=x5^x6^x7
  xx1=x1^x1prim
  xx2=x2^x2prim
  xx4=x4^x4prim
  
    
  S=xx1*m.pow(2,0)*xx2*m.pow(2,1)+xx4*m.pow(2,2)
  SS=int(S)
  
  if SS != 0 and flaga==0:
      print("bledna wartosc w x",SS)
      flaga=flaga+1
      d=sl3[SS-1]
      
      if d==1:
          print(sl3)
          sl3[SS-1]=0
          print("Po przestawieniu ",sl3)
      else:
          sl3[SS-1]=1
          
    
      
  else:
      print("Wiadomosc jest poprawna")
      break
  

        
    
        

#0 brak błedów