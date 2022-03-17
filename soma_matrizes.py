# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 15:11:34 2021

@author: abeln
"""

# soma Matrizes

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

def soma_matrizes(A, B):
    num_lin_A = len(A)
    num_col_A = len(A[0])
    num_lin_B = len(B)
    num_col_B = len(B[0])
    
    if (num_lin_A != num_lin_B) or (num_col_A != num_col_B):
        return False
    
    C = criaMatriz(num_lin_A, num_col_A, 0)
    for lin in range(num_lin_A):
        for col in range(num_col_A):
            C[lin][col] = A[lin][col] + B[lin][col]
    return C

'''if __name__ == "__main__":
    A = [[1, 2, 3], [4, 5, 6]]
    B = [[2, 3, 4], [5, 6, 7]]
    print(soma_matrizes(A, B))
    A = [[1], [2], [3]]
    B = [[2, 3, 4], [5, 6, 7]]
    print(soma_matrizes(A, B))
'''   
    