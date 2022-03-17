# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 17:39:15 2021

@author: abeln
"""
import pytest

def fatorial(n):
    if n < 1:
        return 1
    else:
        return n * fatorial(n-1) #chamada recursiva
    
    
@pytest.mark.parametrize("entrada, esperado", [
   (0, 1),
   (1, 1),
   (2, 2),
   (3, 6),
   (4, 24),
   (5, 120)
   ])

def test_fatorial(entrada, esperado):
    assert fatorial(entrada) == esperado
    