def conta_digitos(n):
    s = str(n)
    digitos = 0
    for caracter in s:
        digitos += 1
    return digitos


def conta_digitos(n):
    digitos = 1
    while n // 10 != 0:
        n = n // 10
        digitos += 1
    return digitos


def conta_digitos(n):
    digitos = 1
    verificador = 10
    while n >= verificador:
        verificador *= 10
        digitos += 1
    return digitos