# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 15:18:21 2022

@author: abeln
"""

def ordenada(lista):
    tam = len(lista) - 1
    for i in range(tam):
        if not(lista[i] < lista[i + 1]):
            return False
    return True
            
'''
lista = [1, 2, 3, 4, 5, 6, 7 , 8, 9]
print(ordenada(lista))
lista = [1, 2, 0, 4, 5, 6, 7 , 8, 9]
print(ordenada(lista))
lista = [9, 8, 7, 6, 5, 4, 3 , 2, 1]
print(ordenada(lista))
lista = [1, 2, 3, 4, 5, 6, 7 , 8, 0]
print(ordenada(lista))
'''