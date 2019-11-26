# -*- coding: UTF-8 -*-
import math
 
a = input("Digite um valor para A: ")
b = input("Digite um valor para B: ")
c = input("Digite um valor para C: ")
 
delta = b * b - 4 * a * c
 
if delta < 0:
    print u"A equação não possui raizes reais"
elif delta == 0:
    raiz = (-1 * b + math.sqrt(delta)) / (2 * a)
    print u"A raiz da equação é: ",raiz
else:
    raiz1 = (-1 * b + math.sqrt(delta)) / (2 * a)
    raiz2 = (-1 * b - math.sqrt(delta)) / (2 * a)   
    print u"As raizes são",raiz1," e ",raiz2c