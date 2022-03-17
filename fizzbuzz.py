# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 09:56:45 2021

@author: abeln
"""

num = int(input("Digite um número inteiro: "))
if(num % 3 == 0) and (num % 5 == 0):
    print("FizzBuzz")         
else:
    print(num)         
            