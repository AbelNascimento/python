# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 09:56:45 2021

@author: abeln
"""

seg = int(input("Digite um número inteiro: "))

seg_dia = 3600 * 24

dias = seg // seg_dia
r = seg % seg_dia
hora = r // 3600
r = r % 3600
min = r // 60
r = r % 60
seg = r
frase = ""

frase = str(dias) + " dias, "
frase = frase + str(hora) + " horas, "
frase = frase + str(min) + " minutos "
frase = frase + "e " + str(seg) + " segundos."
print(frase)         
   
            