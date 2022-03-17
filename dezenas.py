# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 09:56:45 2021

@author: abeln
"""

num = input("Digite um número inteiro: ")
pos = len(num)
if pos < 2:
    print("O dígito das dezenas é 0")         
else:
    dez = num[pos-2]
    print("O dígito das dezenas é", dez)         
   
            