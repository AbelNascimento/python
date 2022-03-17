# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 09:56:45 2021

@author: abeln
"""
import math

x1 = int(input("Digite o valor para x1: "))
y1 = int(input("Digite o valor para y1: "))
x2 = int(input("Digite o valor para x2: "))
y2 = int(input("Digite o valor para y2: "))

if math.sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2)) >= 10:
    print("longe")         
else:
    print("perto")         
            