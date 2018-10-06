# Função PRIMO E CONTAGEM REGRESSIVA 1

def éPrimo(k):
    ii = 1
    d = 0
    while ii <= n:
        if n%ii == 0:
            ii = ii + 1
            d = d + 1
        else:
            ii = ii + 1
        if d == 2:
            p = 'Primo'
        else:
            p = 'Não Primo'
    return p

n = int(input('Digite n: '))
print(éPrimo(n))

# Contagem Regressiva
def valor_n(x):
    i = n
    ii = n
    while i != 1:
        i = i - 1
        ii = ii - 1
        print(ii)
    return ii





