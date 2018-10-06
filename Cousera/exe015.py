#Variante Sequência de Soma de Números

n = int(input('Quantos números terá sua sequência de somas?'))
i = 1
soma = 0
while i <= n:
    num = int(input('Digite o {}º número a ser somado: '.format(i)))
    soma = soma + num
    i = i + 1
print('A soma final dos valores é {}'.format(soma))