# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 15:41:10 2021

@author: abeln
"""


def fatorial(n):
    fat = 1
    while (n > 1):
        fat = fat * n
        n = n - 1
    return fat


def numero_binomial(n, k):
    return fatorial(n) / (fatorial(k) * fatorial(n - k))


def teste_fatorial():
    if fatorial(1) == 1:
        print("fatorial funciona para 1")
    else:
        print("fatorial nao funciona para 1")
    if fatorial(2) == 2:
        print("fatorial funciona para 2")
    else:
        print("fatorial nao funciona para 2")
    if fatorial(0) == 1:
        print("fatorial funciona para 0")
    else:
        print("fatorial nao funciona para 0")
    if fatorial(5) == 120:
        print("fatorial funciona para 5")
    else:
        print("fatorial nao funciona para 5")


teste_fatorial()


