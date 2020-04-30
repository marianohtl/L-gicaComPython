# Identificador de Números Pares / Ímpares

n = int(input('Digite um número inteiro: '))
i = n
ii = 1
d = 0

while i != 0:
    if n % ii == 0:
        d = d + 1
        ii = ii + 1
        i = i - 1
    else:
        ii = ii + 1
        i = i - 1

if d == 2:
    print('primo')
else:
    print('não primo')