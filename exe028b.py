#Teste Automatizado da Função Máximo

from random import randint
def teste_maior():
    x = randint(-1000,1000)
    y = randint(-1000,1000)
    m = máximo(x,y)
    print('{} e {} '.format(x,y))
    return(m)


def máximo (x , y):
    if x > y:
        m = x
    else:
        m = y
    return m


print(teste_maior())




