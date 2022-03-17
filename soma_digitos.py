# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 15:48:53 2021

@author: abeln
"""

numero = int(input("Digite um numero inteiro: "))

soma = 0

while numero != 0:
    valor = numero % 10
    soma = soma + valor
    numero = numero // 10
    
print(soma)