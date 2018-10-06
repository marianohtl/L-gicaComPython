# SEMANA 5 - Exercício 2 - Máximo com 3 parâmetros


def maximo(x,y,z):
    if x == y == z:
        m = x
    if x > y:
        if x > z:
            m = x
        else:
            m = z
    if y > x:
        if y > z:
            m = y
        else:
            m = z
    return m

maximo(30,14,10)
maximo(0,-1,1)



