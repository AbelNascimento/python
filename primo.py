# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 19:10:50 2021

@author: abeln
"""

print("*************************************")
print("verifica se o numero digitado é primo")
print("*************************************")

def primo(n):
    fator = 2
    multiplicidade = 0
    while n > 1 and multiplicidade <= 1:
        while n % fator == 0:
            n = int(n / fator)
            multiplicidade = multiplicidade + 1
        fator = fator + 1
    if multiplicidade == 1:
        return True 
    else:
        return False
    
    
numero = int(input("digite um numero > 1: "))
while numero > 0:
    if primo(numero):
        print(numero,"é primo! :)")
    else:
        print(numero, "nao é primo! :(")       
    numero = int(input("digite um numero > 1: "))
            
            