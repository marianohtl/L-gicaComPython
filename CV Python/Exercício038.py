print('\033[1;33m-'*35)
print('         COMPARANDO VALORES')
print('-'*35)
n = int(input('\033[1;37m\nDigite o Primeiro Número: '))
n1 = int(input('Digite o Segundo Número: \033[m'))

if n > n1:
    print('\n\033[1;33m{} é o Maior!'.format(n))
    print('{} é o Menor!'.format(n1))
elif n1 > n:
    print('\n\033[1;33m{} é Maior!'.format(n1))
    print('{} é o Menor!'.format(n))
else:
    print('\n\033[1;33mNão existe valor maior ou menor, ambos os números são iguais.')