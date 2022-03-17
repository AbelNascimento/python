# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 18:38:45 2022

@author: abeln
"""

def maximo(x, y, z):
    if x >= y and x >= z:
        return x
    else:
        if y >= x and y >= z:
            return y
        else:
            return z
    

