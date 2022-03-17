# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 15:59:23 2022

@author: abeln
"""

def computador_escolhe_jogada(n, m):
    if n > (m+1):
        c = n - (m + 1)
        if c > m:
            c = m
    else:
        c = n
        n = 0
    if c == 1:
        print("O computador tirou", c, "peça.")
    else:
        print("O computador tirou", c, "peças.")
    
    return c
    
def usuario_escolhe_jogada(n, m):
    j = m + 1
    while j > m or j < 1:
        j = int(input("Quantas peças? "))
        if j > m or j < 1:
           print("Oops! Jogada inválida! Tente de novo.")
    
    if j == 1:
        print("Voce tirou", j, "peça.")
    else:
        print("Voce tirou", j, "peças.")
    ultimo_jogador = "j"

    return j

    
def partida():
    ultimmo_jogador = " "
    pj = 0
    pc = 0
    n, m = 0, 1
    
    while n < m:
        n = int(input("Quantas peças? "))
        m = int(input("Limite de peças por jogada? "))
            
    inicio = n % (m+1) 
    if  inicio != 0 or n == m:
        print("Computador começa!")
        ultimo_jogador = "j"
    else:
        print("Você começa!")
        ultimo_jogador = "c"

    while n > 0:
        if ultimo_jogador == "c":      
            p = usuario_escolhe_jogada(n, m)
            n = n - p
            ultimo_jogador = "j"
            if n == 0:
                print("Fim do jogo! voce ganhou!")
                pj = 1
            else:
                if n > 1:
                    print("Agora restam", n, "peças no tabuleiro.")
                else:
                    print("Agora resta apenas", n, "peça no tabuleiro.")
        else:
            p = computador_escolhe_jogada(n, m)
            n = n - p
            ultimo_jogador = "c"
            if n == 0:
                print("Fim do jogo! O computador ganhou!")
                pc = 1
            else:
                if n > 1:
                    print("Agora restam", n, "peças no tabuleiro.")
                else:
                    print("Agora resta apenas", n, "peça no tabuleiro.")

    return pj, pc

def campeonato():
    rodada = 1
    p_j, p_c = 0, 0
    while rodada <= 3:
        print("**** Rodada", rodada, "****")
        placar_j, placar_c = partida()
        p_j = p_j + placar_j
        p_c = p_c + placar_c
        rodada = rodada + 1

    print("**** Final do campeonato! ****")

    print("Placar: Você", p_j, "X", p_c, "Computador")

print("Bem-vindo ao jogo do NIM! Escolha:")   
print("1 - para jogar uma partida isolada")
tipo_partida = input("2 - para jogar um campeonato ")

if tipo_partida == "1":
   partida()
else:
   print("Voce escolheu um campeonato!")
   campeonato()
        
