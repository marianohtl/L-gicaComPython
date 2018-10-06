# Exercício 1 pt.2 - Primos  - Semana 7

'''
def n_primos(y):
    número = teto = y
    indice = 0
    while indice <= teto:
        if número%2 == 1 or número == 2:
            print(número)



        número = número - 1
        indice = indice + 1

n_primos(int(input('Digite um número: ')))'''


def n_primo2(y):
    número = y
    indice = 2
    x = 0
    while indice <= número:
        if indice % 2 == 1 or indice == 2:
            x = x + 1

        indice = indice + 1
    return x


print(n_primo2(int(input('Digite um número: '))))