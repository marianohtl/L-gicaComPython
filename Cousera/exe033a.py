#Teste Automatizado - Exercício 3 - Vogais - Semana 5

import random
from random import randint

#Sorteando Letras
def test_vogal():
    lista = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','ç','z','x','c','v','b','n','m']
    n = randint(0,22)
    v = lista[n]
    return v

#Verificador de Vogais
def vogal(x):
    y = 4
    while y != -1:
        lista = ['A','E','I','O','U']
        r = z in lista[y]
        if r == True:
            y = -1
        else:
            y = y - 1
    return r


z = test_vogal()
z = z.upper()
print('Letra Sorteada:',z)
print(vogal(z))