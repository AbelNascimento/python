# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 15:50:39 2022

@author: abeln
"""


def busca(lista, elemento):
    primeiro = 0
    ultimo = len(lista) - 1
    while primeiro <= ultimo:
        meio = (primeiro + ultimo) // 2
        print(meio)
        if elemento == lista[meio]:
            return meio
        else:
            if elemento <= lista[meio]:
                ultimo = meio - 1
            else:
                if elemento >= lista[meio]:
                    primeiro = meio + 1
    return False

"""
def main():
    print("posicao: ", busca(['a', 'e', 'i'], 'e'))
    # deve devolver => 1

    print("posicao:", busca([1, 2, 3, 4, 5], 6))
    # deve devolver => False

    print("posicao: ", busca([1, 2, 3, 4, 5, 6], 4))
    # deve devolver => 3
"""