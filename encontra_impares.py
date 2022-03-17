# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 18:56:54 2022

@author: abeln
"""
#import pytest
def encontra_impares(lista, lista2 = None):
    if lista2 == None:
        lista2 = []
    if len(lista) == 0:
        return lista2
    elemento = lista.pop(0)
    if elemento % 2 != 0:
        lista2.extend([elemento])
        return encontra_impares(lista, lista2)      
    return encontra_impares(lista, lista2)


lista = [1, 2, 3]
print(encontra_impares(lista))
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(encontra_impares(lista))
lista = []
print(encontra_impares(lista))

'''
@pytest.mark.parametrize("lista, esperado", [
   ([1, 2, 3, 4], 10),
   ([10, 20, 30, 40], 100),
   ([5, 10, 15, 20, 30], 80),
   ([0], 0),
   ])

def testa_soma(lista, esperado):
    assert soma_lista(lista) == esperado
'''