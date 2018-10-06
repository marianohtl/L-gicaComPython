# O PRODUTO DE UMA SEQUÊNCIA NUMÉRICA

print('Digite uma sequência numérica terminada em 0.')
i = 1
produto = 1
while i != 0:
    valor = int(input('Digite o número que será multiplicado: '))
    if valor != 0:
        produto = produto * valor
    else:
        print('O produto da sequência dada é {}'.format(produto))
