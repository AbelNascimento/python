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
    
    # retorna o tipo de triangulo
    def tipo_lado(self):
        if self.a == self.b and self.a == self.c:
            return 'equilátero'
        elif self.a != self.b and self.a != self.c:
            return 'escaleno'
        else:
            return 'isósceles'

    #retorna se o triangulo é retangulo
    def retangulo(self):
        # a**2 + b**2 = c**2
        if self.c ** 2 == self.b ** 2 + self.a ** 2:
            return True
        else:
            return False 
        
    def semelhantes(self, t2):
        ra = self.a / t2.a
        rb = self.b / t2.b
        rc = self.c / t2.c
        if ra == rb and ra== rc:
            return True
        else:
            return False 

def main():
    t1 = Triangulo(2, 3, 5)
    t2 = Triangulo(4, 6, 10)
    print(t1.semelhantes(t2))
    # deve devolver True        
    t1 = Triangulo(2, 2, 5)
    t2 = Triangulo(4, 6, 10)
    print(t1.semelhantes(t2))
    # deve devolver False       
    t1 = Triangulo(2, 3, 5)
    t2 = Triangulo(8, 12, 20)
    print(t1.semelhantes(t2))
    # deve devolver True        
        
'''        
def main():
    t = Triangulo(1, 1, 1)
    print(t.tipo_lado())
    t = Triangulo(1, 1, 2)
    print(t.tipo_lado())
    t = Triangulo(1, 3, 2)
    print(t.tipo_lado())
'''   
''' 
def main():
    t = Triangulo(1, 1, 1)
    print(t.retangulo())
    t = Triangulo(1, 3, 5)
    print(t.retangulo())
    t = Triangulo(3, 4, 5)
    print(t.retangulo())
    t = Triangulo(7, 24, 25)
    print(t.retangulo())
    t = Triangulo(6, 8, 10)
    print(t.retangulo())
'''




    