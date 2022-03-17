# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 16:33:45 2021

@author: abeln
"""

def ord_nomes(lista_nomes):
    i = 0
    menor_nome = "zzz"
    while  i < len(lista_nomes):
        nome_atual = lista_nomes[i].lower().strip()
        tam_atual = len(lista_nomes[i])
        if  tam_atual > 2 and menor_nome > nome_atual:
            menor_nome = nome_atual
        i = i + 1
    print("Menor nome: ", menor_nome.capitalize())

def testa_nomes():
     
    lista = ["Andre", "antonio", "pedro", "juca", "helena", "joaquim", "    ivo  "]
    ord_nomes(lista)
    lista = ["", "antonio", "pedro", "juca     ", "helena", "joaquim", " ana "]
    ord_nomes(lista)
    lista = [" ", "antonio", "   pedro    ", "", "helena", "joaquim", "Abel"]
    ord_nomes(lista)
    
testa_nomes()
