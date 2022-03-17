# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 19:10:50 2021

@author: abeln
"""

#======================================
# verifica se o numero digitado é primo 
#======================================

def primo(n):
    fator = 2
    while (n % fator != 0) and (fator <= n / 2):
        fator = fator + 1
    if n % fator == 0 and n > 2:
        return False 
    else:
        return True
    
def n_primos(x):    
    numero = 2
    qtd = 0
    while numero <= x:
        if primo(numero):
            qtd = qtd + 1
        numero = numero + 1
    return qtd            
            