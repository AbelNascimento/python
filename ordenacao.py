# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 09:56:45 2021

@author: abeln
"""

num1 = int(input("Digite um primeiro número inteiro: "))
num2 = int(input("Digite um segundo número inteiro: "))
num3 = int(input("Digite um terceiro número inteiro: "))

if (num3 > num2) and (num2 > num1):
    print("crescente")         
else:
    print("não está em ordem crescente")         
            