# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 18:25:02 2021

@author: abeln
"""

# fibonacci numbers module

def fib(n):
    a, b = 0, 1
    while b < n:
        print(b, end = " ")
        a, b = b, a + b
    print()
    
def fib2(n):
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a + b
    return result

if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))