# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 15:31:47 2021

@author: abeln
"""
import conta_tempos
import time
import ordenador_hibrido

class buscador:
    
    def busca_sequencial(self, lista, x):
        for i in range(lista):
            if x == lista[i]:
                return i
        return -1
    
    def busca_binaria(self, lista, x):
        primeiro = 0
        ultimo = len(lista) - 1
        while primeiro <= ultimo:
            meio = (primeiro + ultimo) // 2
            if x == lista[meio]:
                return meio
            else:
                if x <= lista[meio]:
                    ultimo = meio - 1
                else:
                    if x >= lista[meio]:
                        primeiro = meio + 1
        return -1
    
    def testa_buscador(self, n):
        lista = []
        inicio = time.time()
        c = conta_tempos.contaTempos()
        o = ordenador_hibrido.ordenador()
        lista = c.listaAleatoria(n)
        lista = o.bolha(lista, "a")
        fim = time.time()
        
        print(lista)
        print()
        print("tempo de criaco da lista: ", fim - inicio, "segundos")

       
        x = int(input("digite um numero da lista: "))
        
        inicio = time.time()
        posicao = self.busca_binaria(lista, x)
        fim = time.time()
        if posicao != -1:
            print("encontrou na posicao: ", posicao)
        else:
            print("numero nao encontrado")
        print("Busca binaria demorou ", fim - inicio, "segundos")
        