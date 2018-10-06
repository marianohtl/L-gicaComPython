

def n_primo2(y):
    número = y
    indice = 2
    x = 0
    while indice <= número:
        if indice % 2 == 1 or indice == 2:
            x = x + 1

        indice = indice + 1
    return x
