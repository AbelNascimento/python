# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 18:14:32 2022

@author: abeln
"""

def merge_sort(lista):
    if len(lista) <= 1:
        return lista
    
    meio = len(lista) // 2
    
    lado_esquerdo = merge_sort(lista[:meio])
    lado_direito = merge_sort(lista[meio:])
    
    return merge(lado_esquerdo, lado_direito)
    
def merge(lado_esquerdo, lado_direito):
    if not lado_esquerdo:
        return lado_direito
    
    if not lado_direito:
        return lado_esquerdo
    
    if lado_esquerdo < lado_direito:
        return [lado_esquerdo[0]] + merge(lado_esquerdo[1:], lado_direito)
    
    return [lado_direito[0]] + merge(lado_esquerdo, lado_direito[1:])

def testa_merge_sort():
    print(merge_sort([10, 50, 40, 30, 80, 5, 90, 15]))
    print(merge_sort([10, 50, 40, 30, 0, 1, -3, -5]))
    

