#Desafio033

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Almost there! Digite mais um número: '))

if n1 > n2 and n1 > n3:
    print('O maior número entre {} , {}  e  {}  é: {}.'.format(n1,n2,n3,n1))
else:
    if n2 > n1 and n2 > n3:
        print('O maior número entre {} , {}  e  {}  é: {}.'.format(n1,n2,n3,n2))
    else:
         print('O maior número entre {} , {}  e  {}  é: {}.'.format(n1,n2,n3,n3))


if n1 < n2 and n1 < n3:
    print('O menor número entre {} , {}  e  {}  é: {}.'.format(n1, n2, n3, n1))
else:
     if n2 < n1 and n2 < n3:
        print('O menor número entre {} , {}  e  {}  é: {}.'.format(n1, n2, n3, n2))
     else:
        print('O menor número entre {} , {}  e  {}  é: {}.'.format(n1,n2,n3,n3))