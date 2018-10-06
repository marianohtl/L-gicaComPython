#Aula - Fatorial - Teste Automatizado - Número Binomial


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

# Função Teste de Fatorial
def testa_fatorial():
    if fatorial(1) == 1:
        print('Funciona para 1')
    else:
        print('Não funciona para 1.')
    if fatorial(2) == 2:
        print('Funciona para 2')
    else:
        print('Não funciona para 2')
    if fatorial(0) == 1:
        print('Funciona para 0')
    else:
        print('Não funciona para 0')
    if fatorial(5) == 2:
        print('Funciona para 5')
    else:
        print('Não funciona para 5')
    if fatorial(-1) == print('Não possui fatorial.'):  #linha teste , não faz parte do curso
        print('Funciona para 0.')                      #verificando se o valor é condição com a condição dos Negativos
    else:
        print('Não funciona para 0')


# Função Número Binominal
def número_binomial(n,k):
    return fatorial(n)/ (fatorial(k) * fatorial(n-k))


#print(número_binomial())
#print(fatorial())
#print(testa_fatorial())

