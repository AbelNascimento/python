# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 15:13:22 2021

@author: abeln
"""


def main():
    carro1 = carro("Corsa", 1999, "Cinza", 110)
    carro2 = carro("Idea Adventure", 2012, "Cinza", 130)

    carro1.acelera(40)
    carro2.acelera(60)
    carro1.acelera(100)
    carro2.acelera(140)
    carro1.pare()
    carro2.pare()
    


class carro:
    def __init__(self, modelo, ano, cor, veloc_max):
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.veloc = 0
        self.veloc_max = veloc_max
        
    def imprima(self):
        if self.veloc == 0:
            print("%s %s %d parou" %(self.modelo, self.cor, self.ano))
        elif self.veloc < self.veloc_max:
            print("%s %s esta indo a  %d Km/h" %(self.modelo, self.cor, self.veloc))
        else:
            print("%s %s esta indo muito raaaaapiiiidooooo! %d Km/h" %(self.modelo, self.cor, self.veloc))
           
    def acelera(self, veloc):
        self.veloc = veloc
        if self.veloc < self.veloc_max:
            self.veloc = self.veloc
        else:
            self.veloc = self.veloc_max

        self.imprima()
        
        
    def pare(self):
        
        self.veloc = 0
        self.imprima()
        
        
main()