#Desafio35
from math import fabs

a = int(input('Digite um número que represente uma medida de um dos lados de um triãngulo: '))
b = int(input('Digite a medida referente ao outro lado: '))
c = int(input('Typing the mitters of other side the triangle: '))

n = 0

if fabs(a - b) < c and (a + b) > c:
    print ('Temos um triângulo!')
else:
     if fabs(c - b) < a  and (c + b) > a:
         print('Temos um triângulo!')
     else:
          if fabs(a - c) < b  and (c + a) > b:
               print('Temos um triângulo!')
          else:
               print('Não temos um triângulo!')

# Não compreendi o porquê da ausência da necessidade de verificar o oposto de a-b >>> (b-a)

""" 
if math.fabs(a - b) < c  and (a + b) > c:
    print('As medidas adicionadas formam um triângulo!')
else:
    if math.fabs(b - a) < c and (b + a) > c:
        print('As medidas adicionadas geram um triângulo!')
    else:
        n = n + 1
        print(n)

if math.fabs(c - b) < a and (c + b) > a:
    print('As medidas adicionadas formam um triângulo!')
else:
    if math.fabs(b - c) < a and (b + c) > a:
        print('As medidas adicionadas geram um triângulo!')
    else:
        n = n+1
        print(n)

if math.fabs(a - c) < a and (a + c) > a:
    print('As medidas adicionadas formam um triângulo!')
else:
    if math.fabs(c - a) < a and (c + a) > a:
        print('As medidas adicionadas formam um triÂngulo!')
    else:
        n = n+1
        print(n)

if n == 3:
    print('Que pena! Não é possível fazer um triângulo com tais medidas... ')"""
