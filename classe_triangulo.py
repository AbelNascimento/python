# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4 18:13:31 2022

@author: abeln
"""

class Triangulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        
        
    def perimetro(self):       
        p = self.a + self.b + self.c
        return p
    
    def tipo_lado(self):
        if self.a == self.b and self.a == self.c:
            return 'equilátero'
        elif self.a != self.b and self.a != self.c:
            return 'escaleno'
        else:
            return 'isósceles'
'''        
def main():
    t = Triangulo(1, 1, 1)
    print(t.tipo_lado())
    t = Triangulo(1, 1, 2)
    print(t.tipo_lado())
    t = Triangulo(1, 3, 2)
    print(t.tipo_lado())
'''    





    