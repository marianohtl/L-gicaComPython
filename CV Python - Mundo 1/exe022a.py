"""co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) **(1/2)
print('A hipotenusa vaimedir {:.2f}.'.format(hi))"""""



#import math
from math import hypot

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = hypot(ca,co)  # import math <math.hypot>
print('A hipotenusa vai medir {:.2f}'.format(hi))

