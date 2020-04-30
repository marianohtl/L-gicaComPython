# Fatorial  - Semana 7

def fatorial(y):
    indice = y
    sequência = 1
    f = 1
    while sequência <= indice:
        f = sequência * f
        sequência = sequência + 1
    return(f)


resposta = True
while resposta != False:
    x = fatorial(int(input('Digite um número: ')))
    print('O fatoria deste número é {}'.format(x))
    r = input('Deseja continuar? [S/N]\n').upper()
    if r == 'N':
        resposta = False















# Versão da Aula

'''
n = int(input('Digite um número inteiro: '))
while n >= 0:
    fatorial = 1
    while n > 1:
        fatorial = fatorial * n
        n = n - 1
    print(fatorial)
    n = int(input('Digite um número inteiro: '))'''


