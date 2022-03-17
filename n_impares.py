# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 15:22:29 2021

@author: abeln
"""

n = int(input("Digite o valor de n: "))
i = 0
c = 1

while (c <= n):
    if i % 2 != 0:
        print (i)
        c = c + 1
    i = i + 1

