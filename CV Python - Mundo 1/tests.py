#----------------------------------test 5
import emoji
print(emoji.emojize("Te amo! :stuck_out_tongue:",use_aliases=True))
print(emoji.emojize('Olá, Mundo.:earth_asia:',use_aliases=True))

#----------------------------------test 4
# #números aleatórios
import random
num = random.random()
print(num)
#números inteiros aleatórios > 1 a 10 <
num2 = random.randint(1,10)
print(num2)
#-------------------------------------- test 3
import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {:.3}.'.format(num,raiz))
# or mat.ceil arredondando para cima
print('A raiz de {} é igual a {}.'.format(num,math.ceil(raiz)))
#or math.floor - arredondando para baixo
print('A raiz de {} é igual a {}.'.format(num,math.floor(raiz)))

from math import sqrt
# from import math sqrt = traz o método indicado diretamente na pasta
print (pow(3,2))
#---------------------------------------- test 2
algo = input('Digite algo: ')
print('{} é do tipo numérico?'.format(algo),algo.isnumeric())

algo = input ('Digite algo: ')
print ('{} é do tipo caracter?'.format(algo),algo.isalpha())

algo = input ('Digite algo: ')
print ('{} é do tipo alphanumérico?'.format(algo),algo.isalnum())
#--------------------- test 1

n = float(input('Digite um valor: '))
print(n)

print('Valor do tipo:',type(n))

n2 = str(input('Digite um valor: '))
print (n2)
print('Valor do tipo:',type(n2))

n3 = bool(input('Digite um valor: '))
print (n3)
print('Valor do tipo:',type(n3))

#-------------------- test 0
n1 = input('Digite um valor: ')
print(type(n1))

num1 = (input('Digite o primeiro valor: '))
num2 = (input('Digite o segundo valor: '))
s = num1+num2
print ('A soma dos valores é',s)

n2 = int(input('Digite um valor: '))
print(type(n2))

num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))
s = num1+num2
print ('A soma dos valores é',s)

num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))
s = num1+num2
print ('A soma dos valores é {}.'.format(s))

num1 = int(input('Digite primeiro valor: '))
num2 = int(input('Digite o segunto valor: '))
s = num1+num2
print('A soma entre {} e {} é {}.'.format(num1, num2, s))

num1 = int(input('Digite primeiro valor: '))
num2 = int(input('Digite o segunto valor: '))
s = num1+num2
print(f'A soma entre {num1} e {num2} é {s}.')
#----------------------------------------------------
n1 = input ("Digite um número: ")
n2 = input ("Digite um número: ")
n3 = n1 + n2
print ("A soma entre", n1, "e", n2 ,"é", n3)

#----------------------
dia = input("Dia = ")
mes = input ("Mês = ")
ano = input ("Ano = ")
print ("Você nasceu no dia",dia,"de",mes,"de",ano,". Correto?")
#--------------------
nome = input ("Qual é o seu nome? ")
idade = input ("Qual é a sua idade? ")
peso = input ("Qual é o seu peso? ")
print (nome, idade, peso)



