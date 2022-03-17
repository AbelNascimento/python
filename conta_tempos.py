# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 14:09:55 2021

@author: abeln
"""
import time
import random
import ordenador_hibrido

class contaTempos:
    
    def listaAleatoria(self, n):
        lista = [random.randrange(n) for x in range(n)]
        return lista    
    
    def comparaLista(self, n):
        lista1 = self.listaAleatoria(n)
        lista2 = lista1[:]
        
        o = ordenador_hibrido.ordenador()
        
        antes = time.time()
        o.bolha(lista1, 1)
        depois = time.time()
        print("Ordenacao Bolha demorou ", depois - antes, "segundos")
        
        antes = time.time()
        o.selecao_direta(lista2, 1)
        depois = time.time()
        print("Ordenacao Selecao direta demorou ", depois - antes, "segundos")
        
        