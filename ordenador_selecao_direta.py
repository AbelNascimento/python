# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 15:51:34 2021

@author: abeln
"""

class ordenador:
    def selecao_direta(self, lista, asc_desc):
        fim = len(lista)
        if asc_desc == "a":
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
    
    def bolha(self, lista, asc_desc):
        fim = len(lista)
        if asc_desc == "a":
            for i in range(fim - 1, 0, -1):
                for j in range(i):
                   if lista[i] < lista[j]:
                       lista[i], lista[j] = lista[j], lista[i]
        else:
             for i in range(fim - 1, 0, -1):
                for j in range(i):
                   if lista[i] > lista[j]:
                       lista[i], lista[j] = lista[j], lista[i]        
       
#### test ordenacao por selecao direta
def testa_ordenador1():
    o = ordenador()
    lista = [19, 2, 5, 1, 10, 30, 50, -10, 300, 340, 40, 45 , 68, 76, 99, 67, 44, 32, 23]
    print(lista)
    o.selecao_direta(lista, "a")       
    print(lista)
    
def testa_ordenador2():
    import random
    o = ordenador()
    lista = []
    i = 0
    while i <= 1000:
        lista.append(random.randint(1, 1000))
        i = i + 1
    print("lista desordenada2:")
    print(lista)
    o.selecao_direta(lista, "a")       
    print("lista ordenada2:")
    print(lista)  
    
def testa_ordenador3():
    o = ordenador()
    lista = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm',
             'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M']
    print("lista desordenada3:")
    print(lista)
    o.selecao_direta(lista, "d")       
    print("lista ordenad32:")
    print(lista) 

#### tes ordenacao bolha ####    
def testa_bolha1():
    o = ordenador()
    lista = [19, 2, 5, 1, 10, 30, 50, -10, 300, 340, 40, 45 , 68, 76, 99, 67, 44, 32, 23]
    print(lista)
    o.bolha(lista, "d")       
    print(lista)
    
def testa_bolha2():
    import random
    o = ordenador()
    lista = []
    i = 0
    while i <= 1000:
        lista.append(random.randint(1, 1000))
        i = i + 1
    print("lista desordenada2:")
    print(lista)
    o.bolha(lista, "a")       
    print("lista ordenada2:")
    print(lista)  
  
def testa_bolha3():
    o = ordenador()
    lista = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm',
             'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M']
    print("lista desordenada3:")
    print(lista)
    o.bolha(lista, "a")       
    print("lista ordenad32:")
    print(lista) 
