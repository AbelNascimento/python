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
    
    @pytest.mark.parametrize("a, b, c, num_raizes, r1, r2", [
        (10, 20, 10, 1, -1),
        (10, 10, 10, 0),
        (10, 25, 10, 2, -0.5, -2),
        ])
        
    def test_uma_raiz(self, a, b, c, num_raizes, r1, r2):
        assert b.calcula_raizes(a, b, c) == (num_raizes, r1, r2)
 
        
        
    
        