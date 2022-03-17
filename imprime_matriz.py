# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 16:59:40 2022

@author: abeln
"""

def  imprime_matriz(matriz):
    lin = len(matriz)
    col = len(matriz[0])
    for i in range(lin):
        for j in range(col):
            if j < col - 1:
                print(matriz[i][j], end = " ")
            else:
                print(matriz[i][j])
                
        
        
        
