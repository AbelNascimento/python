# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 15:33:37 2022

@author: abeln
"""

def busca(lista, x):
    for i in range(len(lista)):
        if x == lista[i]:
            return i
    return False

'''
print(busca(['a', 'e', 'i'], 'e'))
# deve devolver => 1
print(busca(['a', 'e', 'i', 'o', 'u'], 'u'))
# deve devolver => 1
print(busca([12, 13, 14], 15))
# deve devolver => False
print(busca([12, 13, 14, 1, 2], 2))
# deve devolver => False
'''