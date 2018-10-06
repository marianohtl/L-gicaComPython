#Fórmula de Bhaskara

from math import sqrt
a = int(input('Digite o valor de a: '))
b = int(input('Digite o valor de b: '))
c = int(input('Digite o valor de c: '))
delta = b**2-4*a*c
if delta == 0:
    x = (-b + sqrt(delta)) / (2 * a)
    print('a raiz desta equação é {}'.format(x))
else:
    if delta < 0:
        print('esta equação não possui raízes reais')
    else:
        x = (-b + sqrt(delta)) / (2 * a)
        y = (-b - sqrt(delta)) / (2 * a)
        if x < y:
            print('as raízes da equação são {} e {}'.format(x,y))
        else:
            print('as raízes da equação são {} e {}'.format(y,x))