# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 18:18:56 2022

@author: abeln
"""

def menor_nome(lista_nome):
    tam = len(lista_nome)
    tam_menor_nome = len(lista_nome[0].strip())
    menor_nome = lista_nome[0].strip()
    for nome in lista_nome:
        if len(nome.strip()) < tam_menor_nome:
            tam_menor_nome = len(nome.strip())
            menor_nome = nome.strip()
    return menor_nome.capitalize()


'''
def teste_menor_nome():
    lista = ['maria', 'josé', 'PAULO', 'Catarina']
    print(menor_nome(lista))
    lista = ['maria', ' josé ', '   PAULO', 'Catarina   ']
    print(menor_nome(lista))
    lista = ['LU   ', ' josé ', 'PAULO', 'Catarina']
    print(menor_nome(lista))
    lista = ['zé', ' lu', 'fê']
    print(menor_nome(lista))
    lista = ["Cassio  ", "Antonio", "joaquim  ", "  Carla"]
    print(menor_nome(lista))
    lista = ["Cassio  ", "Telmo", "Berilo  ", "  Beatriz"]
    print(menor_nome(lista))
'''