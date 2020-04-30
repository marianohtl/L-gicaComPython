# Soma da Sequência dos Componentes de um Número
n = input('Digite um número: ')
c = int(len(n))
i = 0
n = int(n)
d = 10
d2 = 1
n2 = 0
s = 0
while i <= c:
    i = i + 1
    n1 = n%d
    n3 = n1//d2
    d2 = 10 * d2
    d = 10 * d
    s = s + n3
print('A soma dos algarismos é {}.'.format(s))
