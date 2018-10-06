# SEMANA 5 - Exercício 2 - Primos
def maior_primo(k):
    ii = 1
    iii = k
    d = 0
    l = k
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


maior_primo(100)
maior_primo(7)