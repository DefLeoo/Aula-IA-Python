# -*- coding: UTF-8 -*-
#import math

from math import sqrt
import matplotlib.pyplot as plt

# a = input ("Valor A")
# b = input ("Valor B")

a = float (input("Valor A:"))
b = float (input("Valor B:"))
c = float (input("Valor C:"))

b2 = b**2
delta = b2 - (4*a*c)

try:
    raizquadrada = sqrt(delta)
    x1 = (-b-raizquadrada)/(2*a)
    x2  = (-b + raizquadrada)/(2*a)
    print ("x1="+ str(x1))
    print ("x2="+ str(x2))

except Exception as e:
    print(e)  


eixoX=[]
eixoY=[]

for x in range(-5,5,1):
    y = (a*(x**2)) + (b*x) + c
    eixoX.append(x)
    eixoY.append(y)

fig=plt.figure()
axes=fig.add_subplot(1, 1, 1)
axes.plot(eixoX, eixoY)
plt.show()    



      
