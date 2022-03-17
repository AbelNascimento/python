# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 17:16:15 2022

@author: abeln
"""

def sao_multiplicaveis(A, B):
    num_lin_A = len(A)
    num_col_A = len(A[0])
    num_lin_B = len(B)
    num_col_B = len(B[0])
    if num_col_A == num_lin_B:
        return True
    else:
        return False
    
