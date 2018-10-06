# Semana 5 - Exercício 3 - Vogais

def vogal(x):
    y = 4
    while y != -1:
        lista = ['A','E','I','O','U']
        r = lista[y] in v1
        if r == True:
            y = -1
        else:
            y = y - 1
    return r

v = input('Digite uma Vogal: ')
r = v.isalpha()

if r == True:
    v1 = v[0].upper()
    print(vogal(v1))
else:
    print('Não estamos trabalhando com uma vogal!')