# Soma da Sequência dos Componentes de um Número
n = input('Digite um número: ')
c = int(len(n))
i = 0
ii = 0
soma = 0
while i < c:
    num = int(n[ii])
    soma = soma + num
    i = i + 1
    ii = ii + 1

print('A soma dos algarismos é {}.'.format(soma))