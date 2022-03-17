# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 16:35:57 2021

@author: abeln
"""

print("Exibe uma lista digitada na ordem inversa a digitada")
print("***********************************************************")

i = 0
lista = []
numero = int(input("digite um numero (0 para sair): "))

while numero != 0:
    lista.append(numero)
    i = i + 1
    numero = int(input("digite um numero (0 para sair): "))
    
i = len(lista)
print("Tamanho da Lista Digitsda: ", i)
while i > 0:
    i = i - 1
    print (lista[i], end = " ")
