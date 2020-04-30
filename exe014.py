# Laço White e Soma de Sequência Numérica

print('Digite um sequência de valores terminada por zero.')
valor = 1
soma = 0
while valor != 0:
    valor = int(input('Digite um valor a ser somado: '))
    soma = soma + valor

print('A soma dos valores digitados é: {}'.format(soma))