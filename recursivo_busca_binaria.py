# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 15:50:39 2022

@author: abeln
"""

import pytest

def busca_binaria(lista, elemento, min=0, max=None):
    if max == None:
        max = len(lista) - 1
    if max < min:
        return False
    else:
        meio = min + (max - min) // 2
    
    if lista[meio] > elemento:
        return busca_binaria(lista, elemento, min, meio - 1)
    elif lista[meio] < elemento:
        return busca_binaria(lista, elemento, meio + 1, max)
    else:
        return meio

a = [-10, -2, 0, 5, 66, 77, 99, 102, 239, 567, 875, 934]

busca_binaria(a, 99)

@pytest.mark.parametrize("lista, elemento, esperado", [
   (a, 10, 0),
   (a, 20, 1),
   (a, 30, 2),
   (a, 40, 3),
   (a, 50, 4),
   (a, 60, 5),
   (a, 70, False),
   (a, 15, False),
   (a, 35, False),
   ])

def test_fatorial(lista, elemento, esperado):
    assert busca_binaria(lista, elemento) == esperado
