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
    
    
numero = int(input("digite um numero > 1: "))
while numero > 0:
    if primo(numero):
        print(numero,"é primo! :)")
    else:
        print(numero, "nao é primo! :(")       
    numero = int(input("digite um numero > 1: "))
            
            