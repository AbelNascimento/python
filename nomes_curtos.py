# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 15:02:47 2021

@author: abeln
"""


def nomes_curtos(lista_nomes):
    i = 0
    tam_nome = 99
    menor_nome = " "
    while  i < len(lista_nomes):
        tam_atual = len(lista_nomes[i].strip()) 
        if  tam_atual > 2 and tam_atual < tam_nome:
            menor_nome = lista_nomes[i].strip()
            tam_nome = tam_atual
        i = i + 1
    print("Menor nome: ", menor_nome.capitalize(), "Tamanho: ", tam_nome)

def testa_nomes():
     
    lista = ["Andre", "antonio", "pedro", "juca", "helena", "joaquim", "    ivo  "]
    nomes_curtos(lista)
    lista = ["", "antonio", "pedro", "juca     ", "helena", "joaquim", ""]
    nomes_curtos(lista)
    lista = [" ", "antonio", "   pedro    ", "", "helena", "joaquim", ""]
    nomes_curtos(lista)
    
testa_nomes()
