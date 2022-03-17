# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 16:35:57 2021

@author: abeln
"""
def remove_repetidos(lista):
    lista2 = []
    c = len(lista)
    for i in range(0, c):
          if lista[i] not in lista2:
              lista2.append(lista[i])
    lista = sorted(lista2)
    return lista


    
def sorted(lista):
    fim = len(lista)
    for i in range(fim - 1, 0, -1):
        for j in range(i):
            if lista[i] < lista[j]:
                lista[i], lista[j] = lista[j], lista[i]
    return lista


            
            
                
    
