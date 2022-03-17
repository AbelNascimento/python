# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 17:32:41 2021

@author: abeln
"""

def criaMatriz(num_linhas, num_colunas):
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
            valor = int(input("Digite o valor do elemento [" + str(i) + "] [" + str(j) + "] "))
            linha.append(valor)
        matriz.append(linha)
    
    return matriz

linha = int(input("digite numero de linhas: "))
coluna = int(input("digite numero de colunas: "))

matriz = criaMatriz(linha, coluna)

for i in range(linha):
    print (matriz[i])


