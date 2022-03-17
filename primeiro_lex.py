# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 18:18:56 2022

@author: abeln
"""

def primeiro_lex(lista_string):
    tam = len(lista_string)
    menor_string = lista_string[0].strip()
    for i in range(tam):
        if lista_string[i].strip() < menor_string:
            menor_string = lista_string[i].strip()
    return menor_string



print(primeiro_lex(['oĺá', 'A', 'a', 'casa']))
# deve devolver 'A'

print(primeiro_lex(['AAAAAA', 'b']))
# deve devolver 'AAAAAA'