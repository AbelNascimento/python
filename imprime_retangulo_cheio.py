# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 16:01:45 2022

@author: abeln
"""

largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))
x = 1     
while x <= altura:
    y = 1        
    while y <= largura:
        print("#", end="")
        y+=1
                     
    print()
    x+=1