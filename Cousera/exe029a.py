# Função Teste Binomial


#Função Fatorial
def fatorial(n):
    fat = 1
    while (n > 1):
        fat = fat * n
        n = n - 1
    if n < 0:
        print('Não possui fatorial.')
    else:
        return fat

# Função Número Binominal
def número_binomial(n,k):
    return fatorial(n)/ (fatorial(k) * fatorial(n-k))

print(número_binomial(6,2))

#Função Teste Binomial
def test_Binomial():
    if número_binomial(9,4) == 126:
        print('Funciona para 9 e 5.')
    else:
        print('Não funciona para 9 e 4.')
    if número_binomial(8,2) == 28:
        print('Funciona para 8 e 2.')
    else:
        print('Não funciona para 8 e 2.')
    if número_binomial(7,5) == 21:
        print('Funciona para 7 e 5.')
    else:
        print('Não funciona para 7 e 5.')

    if número_binomial(9,8) == 9:
        print('Funciona para 9 e 8.')
    else:
        print('Não funciona para 9 e 8.')

    if número_binomial(8,5) == 56:
        print('Funciona para 8 e 5.')
    else:
        print('Não funciona para 8 e 5.')

    if número_binomial(4,2) == 6:
        print('Funciona para 4 e 2.')
    else:
        print('Não funciona para 4 e 2.')

    if número_binomial(6,4) == 15:
        print('Funciona para 6 e 4.')
    else:
        print('Não funciona para 6 e 4.')

    if número_binomial(1,1) == 1:
        print('Funciona para 1 e 1.')
    else:
        print('Não funciona para 1 e 1.')

    if número_binomial(1,0) == 1:
        print('Funciona para 1 e 0.')
    else:
        print('Não funciona para 1 e 0.')

    if número_binomial(0,0) == 1:
        print('Funciona para 0 e 0.')
    else:
        print('Não funciona para 0 e 0.')

print(test_Binomial())