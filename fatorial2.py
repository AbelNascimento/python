# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 15:22:29 2021

@author: abeln
"""

print("calcula o fatorial de um numero duigitado")
n = int(input("digite um numero positivo ou negativo para sair: "))
while n >= 0:
    fat = 1
    while (n > 1):
        fat = fat * n
        n = n - 1
    print("fatorial = ", fat)
    n = int(input("digite um numero positivo ou negativo para sair: "))
        

