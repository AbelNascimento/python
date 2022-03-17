# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 15:44:14 2022

@author: abeln
"""
import random

def lista_grande(tam):
    i = 0
    # cria lista com tamanho 'tam'
    lista = []
    for i in range(tam):
        lista.append(random.randrange(tam))
    return lista

print(lista_grande(0))
print(lista_grande(1))
print(lista_grande(100))
