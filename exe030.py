# Função PRIMO E CONTAGEM REGRESSIVA 2

def primo(k):
    ii = 1
    iii = n
    d = 0
    while ii <= iii:
        if n % ii == 0:
            ii = ii + 1
            d = d + 1
        else:
            ii = ii + 1
    return d


#Contagem Regressiva
def valor_n(x):
    i = n
    ii = n
    while i != 0:
        print(ii)
        i = i - 1
        ii = ii - 1
    return ii


p = 0
n = int(input('Digite um número inteiro >= 2: '))
if n >=2:
    primo(n)
else:
    print('Número Inválido! ')

if primo(n) == 2:
    p = p + 1
    print(p)
else:
    print('error')

valor_n(n)
