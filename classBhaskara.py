# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 09:56:45 2021

@author: abeln
"""
import math

class Bhaskara:
    def main(self):
        a = int(input("digite a: "))
        b = int(input("digite b: "))
        c = int(input("digite c: "))

        print(self.calcula_raizes(a, b, c))
        
   
    def calcula_raizes(self, a, b, c):
        delta = int(b ** 2 - 4 * a * c)
        if delta < 0:
            return 0 

        else:
            x1 = (- b + math.sqrt(delta)) / (2 * a)
            if delta == 0:
                return 1, x1
            else:
                x2 = (-b - math.sqrt(delta)) / (2 * a)
                return 2, x1, x2
            