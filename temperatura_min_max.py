# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 16:34:00 2021

@author: abeln
"""
def temp_min_max(temps, min_max):
    temp_fin = temps[0]
    i = 1
    while i < len(temps):
        if min_max == 0:
            if temps[i] < temp_fin:
                temp_fin = temps[i]
        else:
            if temps[i] > temp_fin:
                temp_fin = temps[i]
        i = i + 1
    return temp_fin

def testa_temp(temperatura, valor_esperado, min_max):
    '''min_max: 0 = min / 1 = max'''
    temp_ret = temp_min_max(temperatura, min_max)
    if temp_ret != valor_esperado:
        print ("valor esperado: ", valor_esperado, "C.")
        print ("valor retornado: ", temp_ret, "C.")
    

def testa_min():
    testa_temp([0], 0, 0)
    testa_temp([1], 1, 0)
    testa_temp([0, 0, 0, 0, 0], 0, 0)
    testa_temp([1, 2, 3, 4, 5], 1, 0)
    testa_temp([22, 22, 22, 22], 22, 0)
    testa_temp([22, 25, 27, 30, 21, 22, 35, 37, 28, 24, 25, 25, 26, 27, 28, 20], 20, 0)
    testa_temp([-10, -12, 0, 10, 20], -12, 0)

def testa_max():
    testa_temp([0], 0, 1)
    testa_temp([1], 1, 1)
    testa_temp([0, 0, 0, 0, 0], 0, 1)
    testa_temp([1, 2, 3, 4, 5], 5, 1)
    testa_temp([22, 22, 22, 22], 22, 1)
    testa_temp([22, 25, 27, 30, 21, 22, 35, 37, 28, 24, 25, 25, 26, 27, 28, 20], 37, 1)
    testa_temp([-10, -12, 0, 10, 20], 20, 1)


