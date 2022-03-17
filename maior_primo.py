# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 18:38:45 2022

@author: abeln
"""

def éprimo(n):
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
   
def maior_primo(n):
    while not éprimo(n) and n > 2:
        n = n - 1
    return n    
        
        

