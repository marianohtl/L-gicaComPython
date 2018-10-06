]#Desafio33

a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
# Verificando Quem é Menor
if a < b and a < c:
    menor = b
if c < a and c < b:
    menor = c
# Verificando Quem é Maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O menor valor digitado foi {}.'.format(menor))
print('O maior valor digitado foi {}.'. format(maior))