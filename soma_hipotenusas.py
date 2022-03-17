# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 19:10:50 2021

@author: abeln
"""

#======================================
# soma hipotenusas a partira de um numero recebido 
# As hipotenusas do numero 25 sao:
# 5 10 13 15 17 20 25
# A soma = 105
#======================================

def é_hipotenusa(n):
    i = 1
    while i <= n:
        j = 1
        while j <= n:
            if n**2 == i**2 + j**2:
               return True
            j+=1
        i+=1
    return False
    
def soma_hipotenusas(x):
    y = 1
    soma = 0
    while y <= x:
        if é_hipotenusa(y):
            soma = soma + y
        y+=1
    return soma            
            
soma_hipotenusas(25)