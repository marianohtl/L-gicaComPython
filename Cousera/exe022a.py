#Números Adjacentes Iguais
sequência = input('Digite uma Sequência Numérica: ')

length = len(sequência)
i = 0
n2 = 0
determinante = 0
while length != 0:
    length = length - 1
    n1 = sequência[i]
    i = i + 1
    if n1 == n2:
        determinante = 1
        n2 = n1
    else:
        n2 = n1


if determinante == 1:
    print('sim')
else:
    print('não')