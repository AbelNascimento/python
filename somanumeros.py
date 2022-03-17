# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 15:48:53 2021

@author: abeln
"""

print("calcula a soma de cada unidade do numero digitado")
print("*************************************************")
numero = int(input("digite um numero: "))

soma = 0

while numero != 0:
    valor = numero % 10
    soma = soma + valor
    numero = numero // 10
    
print("resultado da soma dos numeros: ", soma)