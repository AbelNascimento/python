# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 19:10:50 2021

@author: abeln
"""


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
    
    
numero = int(input("Digite um número inteiro: "))
if primo(numero):
    print("primo")
else:
    print("não primo")       
            
            