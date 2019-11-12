# -*- coding: UTF-8 -*-
#import math

from math import sqrt

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