# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 16:35:57 2021

@author: abeln
"""

print("Verifica se a sequencia de numeros possui adjacentes iguais")
print("***********************************************************")
numero = int(input("digite um numero: "))

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
    print("Achei numeros adjacentes")   
else:
    print("Nao achei numeros adjacentes")   
