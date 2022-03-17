# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 16:35:57 2021

@author: abeln
"""

numero = int(input("Digite um número inteiro: "))

soma = 0
possuiNumeroAdjacente = False
valorAnterior = 11

while numero != 0 and not possuiNumeroAdjacente:
    valor = numero % 10
    if valor == valorAnterior:
        possuiNumeroAdjacente = True
    numero = numero // 10
    valorAnterior = valor
if possuiNumeroAdjacente:
    print("Sim")   
else:
    print("Não")   
