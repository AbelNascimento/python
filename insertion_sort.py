# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 16:58:50 2022

@author: abeln
"""

def insertion_sort(lista):
    fim = len(lista)
    for i in range(fim - 1):
        ind_minimo = i
        for j in range(i+1, fim):
            if lista[j] < lista[ind_minimo]:
                ind_minimo = j
                    
        lista[i], lista[ind_minimo] = lista[ind_minimo], lista[i]
    return lista