# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 15:22:29 2021

@author: abeln
"""

multiplicando = 1
multiplicador = 1

while multiplicador <= 10:
    while multiplicando <= 10:
        print(multiplicador * multiplicando, end = '\t')
        multiplicando = multiplicando + 1
    print()
    multiplicador = multiplicador + 1
    multiplicando = 1
