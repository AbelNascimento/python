# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 15:50:07 2022

@author: abeln
"""

def ordena(lista):
    fim = len(lista)
    for i in range(fim - 1):
        ind_minimo = i
        for j in range(i+1, fim):
            if lista[j] < lista[ind_minimo]:
                ind_minimo = j
                    
        lista[i], lista[ind_minimo] = lista[ind_minimo], lista[i]
    return lista
'''
lista = [2, 20, 47, 37, 48, 2, 75, 24, 1, 41, 59, 63, 27, 98, 38, 59, 56, 79, 7, 92, 74, 31, 52, 20, 58, 80, 71, 24, 30, 56, 90, 81, 63, 35, 83, 50, 88, 52, 25, 12, 88, 56, 31, 33, 5, 1, 20, 19, 37, 84, 34, 69, 43, 79, 39, 86, 17, 39, 76, 94, 6, 99, 70, 5, 40, 15, 78, 58, 21, 33, 46, 52, 89, 3, 8, 57, 95, 92, 96, 32, 63, 1, 42, 62, 47, 37, 1, 96, 80, 57, 84, 65, 42, 88, 28, 31, 41, 79, 86, 40, 87]
print(ordena(lista))
lista = [9, 0, 1, 4, 6, 2, 3, 7, 5, 8]
print(ordena(lista))
'''