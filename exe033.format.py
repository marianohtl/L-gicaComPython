# Semana 5 - Exercício 3 - Vogais

def vogal(x):
    y = 4
    x = x.upper()
    while y != -1:
        lista = ['A','E','I','O','U']
        r = lista[y] in x
        if r == True:
            y = -1
        else:
            y = y - 1
    return r

vogal('a')
vogal('b')
vogal('E')
