# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 19:38:18 2022

@author: abeln
"""

def maiusculas(frase):
    tam = len(frase)
    mai = ""
    for i in range(tam):
        if ord(frase[i]) >= 65 and ord(frase[i]) <= 90:
            if frase[i] == frase[i].upper():
                mai = mai + frase[i]
    return mai
                
""" def testa_maiusculas():
    maiusculas('Programamos em python 2?')
    # deve devolver 'P'
    maiusculas('Programamos em Python 3.')
    # deve devolver 'PP'
    maiusculas('PrOgRaMaMoS em python!')
    # deve devolver 'PORMMS'
"""