# SEMANA 5 - TESTE AUTOMATIZADO - Exercício 2 - Máximo com 3 parâmetros

#Máximo1 com 3 Parâmetros + TESTE AUTOMATIZADO
from random import randint
#sorteio dos parâmetros
def test_one ():
    n = randint(-1000,1000)
    return (n)

#maior entre 3 valores
def maximo (x,y,z):
    if x == y == z:
        m = x
    if x > y:
        if x > z:
            m = x
        else:
            m = z
    if y > x:
        if y > z:
            m = y
        else:
            m = z
    return m
n = test_one()
nn = test_one()
nnn = test_one()
print(n,nn,nnn)
print(maximo(n,nn,nnn))



#Máximo2 Com 3 Parâmetros + TESTE AUTOMATIZADO

from random import randint
#sorteio dos parâmetros
def test_one ():
    n = randint(-1000,1000)
    return (n)

#maior entre 3 valores
def maximo2 (x,y,z):
    if x > y > z:
        m = x
    elif x > z > y:
        m = x
    elif y > x > z:
        m = y
    elif y > z > x:
        m = y
    elif z > x > y:
        m = z
    elif z > y > x:
        m = z
    return m


n = test_one()
nn = test_one()
nnn = test_one()
print(n,nn,nnn)
print(maximo2(n,nn,nnn))

