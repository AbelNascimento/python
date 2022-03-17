# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 18:46:20 2022

@author: abeln
"""

def incomodam(n, palavra = ""):
    if n < 0:
        return ""
    elif n == 0:
        return palavra
    else:
        palavra = palavra + "incomodam " 
        n -= 1
        return incomodam(n, palavra)
        
#print(incomodam(10))

def elefantes(n, elefante = [], i = 0):
    if n < 0:
        return ""
    elif n == i:
        ret_elefante = ""
        for i in range(len(elefante)):
            ret_elefante = ret_elefante + elefante[i] 
        return ret_elefante
    elif i == 0:
        elefante.append("Um elefante incomoda muita gente\n")
    else:
        elefante.append(str(i + 1) + " elefantes " + incomodam(i +1) + "muito mais\n")
        if i < n - 1:
            elefante.append(str(i + 1) + " elefantes incomodam muita gente\n")

    i += 1
    return elefantes(n, elefante, i)
    
print(elefantes(-1))