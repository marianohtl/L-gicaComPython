#Desafio032

n = int(input('Digite um ano: '))
if n%100 == 0 and n%400==0:
    print('{} é um ano Bisexto!'.format(n))
else:
    if n%100 >= 1 and n%4 == 0:
        print('{} é um ano Bisexto!'.format(n))
    else:
        print('{} não é um ano Bisexto!'.format(n))


# considera 0 um ano bisexto o