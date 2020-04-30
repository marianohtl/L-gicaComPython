#Teste Automatizado - Exercício 2 - Primos - SEMANA 5

from random import randint

def maior_primo(k):
    ii = 1
    iii = n
    d = 0
    l = n
    chave = 0
    while l >= 0:

        while ii <= iii:
            if iii % ii == 0:
                ii = ii + 1
                d = d + 1
            else:
                ii = ii + 1

        if d == 2:
            chave = iii
            l = 0

        ii = 1
        iii = iii - 1
        l = l - 1
        d = 0

    return chave


n = randint(0,100)
print('O número sorteado é ',n)
if n >=2:
    print('O maior número primo é {}'.format(maior_primo(n)))
else:
    print('Número Inválido! ')