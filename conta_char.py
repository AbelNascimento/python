# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4 15:14:15 2022

@author: abeln
"""

def conta_letras(frase, contar="vogais"):
    tam = len(frase)
    cont_v = 0
    cont_c = 0
    vogais = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]
    tam_v = len(vogais)
    for i in range(tam):
        achou_vogal = False
        asc = ord(frase[i])
        if (ord(frase[i]) >= 65 and ord(frase[i]) <= 90) or (ord(frase[i]) >= 97 and ord(frase[i]) <= 122): 
            for j in range(tam_v):
                if frase[i] == vogais[j]:
                    cont_v += 1
                    achou_vogal = True
            if achou_vogal == False:
                cont_c += 1
            
   
    if contar == "vogais":
        return cont_v
    else:
        return cont_c
                
'''
#def testa_conta_letra():
print(conta_letras('programamos em python'))
    # deve devolver 6

print(conta_letras('programamos em python', 'vogais'))
    # deve devolver 6

print(conta_letras('programamos em python', 'consoantes'))
    # deve devolver 13

print(conta_letras('Antonio foi ao lago nadar e volta ja', 'consoantes'))
    # deve devolver 13
    
print(conta_letras('Antonio foi ao lago nadar e volta ja'))
    # deve devolver 13
'''