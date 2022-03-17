# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 16:56:36 2021

@author: abeln
"""

import classBhaskara
import pytest

class TestBhaskara:
    
    @pytest.fixture
    def b(self):
        return classBhaskara.Bhaskara()
        
    def test_uma_raiz(self, b):
        assert b.calcula_raizes(10, 20, 10) == (1, -1)
    def test_zero_raiz(self, b):
        assert b.calcula_raizes(10, 10, 10) == (0)
    def test_duas_raizes(self, b):
        assert b.calcula_raizes(10, 25, 10) == (2, -0.5, -2)
        
        
        
    
        