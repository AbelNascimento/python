# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 18:18:56 2022

@author: abeln
"""

def menor_string(lista_string):
    tam = len(lista_string)
    menor_string = lista_string[0].strip().lower()
    for i in range(tam):
        if lista_string[i].strip().lower() < menor_string:
            menor_string = lista_string[i].strip().lower()
    return menor_string.capitalize()


'''
def teste_menor_string():
    lista = ["  Ana  ", "Telmo", "joaquim  ", "  Valdemar"]
    print(menor_string(lista))
    lista = ["  Ana  ", "beatriz", "joaquim  ", "  Valdemar"]
    print(menor_string(lista))
    lista = ["  Luiz  ", "Telmo", "joaquim  ", "  Valdemar"]
    print(menor_string(lista))
    lista = ["Cassio  ", "Telmo", "joaquim  ", "  Carla"]
    print(menor_string(lista))
    lista = ["Cassio  ", "Antonio", "joaquim  ", "  Carla"]
    print(menor_string(lista))
    lista = ["Cassio  ", "Telmo", "Berilo  ", "  Beatriz"]
    print(menor_string(lista))
'''    