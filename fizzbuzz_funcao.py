# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 18:40:28 2022

@author: abeln
"""

def fizzbuzz(num):
    if(num % 3 == 0) and (num % 5 == 0):
        return "FizzBuzz"         
    else:
        if num % 3 == 0:
            return "Fizz"
        else:
            if num % 5 == 0:
                return "Buzz"
            else:
                return num         
