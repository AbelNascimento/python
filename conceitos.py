# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 17:23:14 2021

@author: abeln
"""

def conceitos1():
    a, b = 10, 20
    print("a=", a)
    print("b=", b)
    
    print("# inverte os valores #")
    a = 1
    b = 2
    print("a=", a, "b=", b)
    a, b = b, a
    print("a=", a, "b=", b)

    print("# soma 1 #")
    i = 0   
    while i <= 10:
        print("i=", i)
        i += 1

    print("# subtrai 1 #")
    i = 10    
    while i >= 0:
        print("i=", i)
        i -= 1

    print("# multiplica 2 #")
    i = 2   
    while i < 10:
        print("i=", i)
        i *= 2

    print("# divide por 2 #")
    i = 10   
    while i >= 1:
        print("i=", i)
        i /= 2

    print("# exponenciacao por 2 #")
    i = 2    
    while i < 100:
        print("i=", i)
        i **= 2

# torna o segundo parametros opcional (paramnetros opcionais devem ficar no final) 
# atribui um valor default         
def conceitos2(valor_por_hora, hora_semanal = 40):
    # assercao: aborta o programa caoso a(s) condicoes nao seja satisfeitas (AssertinoError)
    assert valor_por_hora > 0 and hora_semanal > 0
    print("# parametros opcionais: ", valor_por_hora, " ", hora_semanal)
    print(valor_por_hora * hora_semanal)
        
conceitos1()

print("sem passar o segundo parametro")
conceitos2(100)

print("passando o segundo parametro")
conceitos2(200, 36)

print("aborta o programa por assert")
conceitos2(-200, 36)

