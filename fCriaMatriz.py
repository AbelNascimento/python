# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 17:32:41 2021

@author: abeln
"""

def criaMatriz(num_linhas, num_colunas, valor):
    ''' 
    criaMatriz(num_linhas, num_colunas, valor)
    onde: 
    num_linhas = numero de linhes
    num_colunas = numero de colunas
    valor = valor com que cada elemento sera inicializad
    '''

    matriz = []

    for i in range(num_linhas):
        linha = []
        for j in range(num_colunas):
            linha.append(valor)
        matriz.append(linha)
    
    return matriz

def testaCriaMatriz():
    linha = 4
    coluna = 5
    valor = 0

    #for i in range(coluna):
        #    valor.append(i)
    
    matriz = criaMatriz(linha, coluna, valor)

    for i in range(linha):
        print (matriz[i])


