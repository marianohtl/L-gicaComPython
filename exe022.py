#desafio017
from math import hypot
print('-'*35)
print ('HYPOTENUSA DO TRIÂNGULO RETÂNGULO')
print('-'*35)
co = float(input('Digite a medida do cateto oposto: '))
ca = float(input('Digite a medida do cateto adjacente: '))
print ('A medida da hypotenusa é {:.3}.'.format(hypot(co,ca)))