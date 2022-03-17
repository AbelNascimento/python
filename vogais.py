# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 17:14:01 2022

@author: abeln
"""

def vogal(letra):
    i = 0
    vogal = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    while i < len(vogal):
        if vogal[i] == letra:
            return True
        else:
            i += 1
    return False
    
    