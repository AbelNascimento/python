# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 17:05:21 2021

@author: abeln
"""

n = int(input("digite um numero > 1: "))
d = 2
quociente = 2
while quociente > 1:
    quociente = int(n / d)
    resto = n % d
    if resto == 0:
        n = quociente
        print(d, end=" ")
        if quociente > 1:
            print("*", end=" ")
    else: 
        d = d + 1
