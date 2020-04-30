# Teste Automatizado da Função MÁXIMO
from random import randint

def test_one ():
    n = randint(-1000,1000)

    return (n)


def máximo (x,y):
    if x > y:
        m = x
    else:
        m = y
    return m

n = test_one()
nn = test_one()
print('entre {} e {}'.format(n,nn))
print('maior == ',máximo(n,nn))
