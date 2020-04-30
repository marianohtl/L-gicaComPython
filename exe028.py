# SEMANA 5 - Exercício 1 - Máximo

def máximo (x , y):
    if x > y:
        m = x
    else:
        m = y
    return m

n = int(input('Digite um número: '))
nn = int(input('Digite o segundo número: '))
print(máximo(n,nn))
