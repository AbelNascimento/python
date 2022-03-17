# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 18:56:54 2022

@author: abeln
"""
#import pytest
def soma_lista(lista):
    fim = len(lista)
    if fim == 1:
        return lista[0]
    else:
        return lista[0] + soma_lista(lista[1:])

#print(soma_lista([10, 20]))

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