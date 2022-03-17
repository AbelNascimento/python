# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 09:56:45 2021

@author: abeln
"""
import math

a = int(input("digite a: "))
b = int(input("digite b: "))
c = int(input("digite c: "))
delta = int(b ** 2 - 4 * a * c)
#print("delta = ", delta)

if delta < 0:
    print ("esta equação não possui raízes reais")
else:
    x1 = (- b + math.sqrt(delta)) / (2 * a)
    if delta == 0:
        print ("a raiz dupla desta equação é", x1)
    #    print("x1 = ", x1)
    else:
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        if x1 < x2:
            print("as raízes da equação são", x1, "e", x2)
        else:
            print("as raízes da equação são", x2, "e", x1)
            