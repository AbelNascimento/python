# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 15:51:34 2021

@author: abeln
"""

class ordenador:
    def selecao_direta(self, lista, ordem):
        print("fazendo sort pela selecao direta")
        fim = len(lista)
        if ordem == "a":
            for i in range(fim - 1):
                ind_minimo = i
                for j in range(i+1, fim):
                   if lista[j] < lista[ind_minimo]:
                       ind_minimo = j
                    
                lista[i], lista[ind_minimo] = lista[ind_minimo], lista[i]
        else:
             for i in range(fim - 1):
                ind_minimo = i
                for j in range(i+1, fim):
                   if lista[j] > lista[ind_minimo]:
                       ind_minimo = j
                    
                lista[i], lista[ind_minimo] = lista[ind_minimo], lista[i]           
    
    def bolha(self, lista, ordem):
        print("fazendo sort pela bolha")
        fim = len(lista)
     #   print("ordem:", ordem)
        if ordem == "a":
            for i in range(fim - 1, 0, -1):
                for j in range(i):
                 #   print(lista[i], " ", lista[j])
                    if lista[j] > lista[j + 1]:
                       lista[j], lista[j + 1] = lista[j + 1], lista[j]
                       trocou = True
                if not trocou:      
                    return lista
        else:
            for i in range(fim - 1, 0, -1):
                trocou = False
                for j in range(i):
                 #   print(lista[i], " ", lista[j])
                    if lista[j] < lista[j + 1]:
                       lista[j], lista[j + 1] = lista[j + 1], lista[j]
                       trocou = True
                if not trocou:      
                    return lista
        return lista
       
# tipo de ordenacao: s = selecao direta / b = bolha
# ordem: a = ascendente / d = descendente   
def testa_ordenador(lista, tam, tipo, ordem):
    import random
    o = ordenador()
    i = 0
    if tam != 0:
        # cria lista com tamanho 'tam'
        lista = []
        for i in range(tam):
            lista.append(random.randrange(tam))
  

    print("lista desordenada:")
    print(lista)
    if tipo == "s":
        o.selecao_direta(lista, ordem)
    else:
        o.bolha(lista, ordem)
    lista2 = lista[:]

    #for i in range(len(lista) - 1):
    #    if lista[i] != lista[i+1]:
    #        lista2.append(lista[i+1])
    #lista = lista2

    print("lista ordenada:")
    print(lista)  
    
def main():
    lista = [19, 2, 5, 1, 10, 30, 50, -10, 300, 340, 40, 45 , 68, 76, 99, 67, 44, 32, 23]
    tam = 0
    tipo = 's'
    ordem = "a"
    testa_ordenador(lista, tam, tipo, ordem)
    
    lista = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm', 'q', 'm',
             'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', 'A', 'J'
             ]
    tipo = 'b'
    ordem = "a"
    testa_ordenador(lista, tam, tipo, ordem)
    
    lista = [21, 73, 72, 27, 11, 77, 58, 76, 96, 95, 99, 69, 95, 27, 88, 53, 94, 38, 64, 0, 6, 59, 76, 55, 17, 9, 90, 69, 93, 91, 51, 67, 87, 42, 28, 74, 47, 59, 82, 93, 21, 87, 92, 55, 29, 27, 44, 10, 73, 36, 81, 87, 94, 41, 19, 55, 87, 65, 85, 33, 12, 41, 61, 8, 4, 12, 49, 51, 3, 20, 34, 32, 65, 87, 55, 88, 1, 97, 56, 87, 53, 15, 94, 63, 96, 16, 81, 74, 74, 37, 3, 88, 87, 17, 29, 30, 80, 70, 22, 45]
    tam = 100
    tipo = 'b'
    ordem = "d"
    testa_ordenador(lista, tam, tipo, ordem)    
    
    