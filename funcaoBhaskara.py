# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 09:56:45 2021

@author: abeln
"""

# Calcula Delta
# =============      
def calcDelta(a, b, c):
    return int(b ** 2 - 4 * a * c)
#==============================================

# Formula de Bhaskara
# ===================
def bhaskara(a, b, c):
    delta = calcDelta(a, b, c)
    if delta < 0:
        print ("equacao nao possui raiz real")
    else:
        x1 = (- b + math.sqrt(delta)) / (2 * a)
        if delta == 0:
            print ("equacao possui uma raiz real")
            print("x1 = ", x1)
        else:
            x2 = (-b - math.sqrt(delta)) / (2 * a)
            print("equacao possui duas raizes reais")
            print("x1 = ", x1)
            print("x2 = ", x2)           
#==============================================

# Main 
# ====
import math

a = int(input("digite a: "))
b = int(input("digite b: "))
c = int(input("digite c: "))
bhaskara(a, b, c)

#==============================================
        
        
