#desafio020
import random

print('-'*35)
print ('     SORTEIO DOS ALUNOS')
print('-'*35)

a1 = input('Digite o nome do primeiro aluno: ')
a2 = input('Digite o nome do segundo aluno: ')
a3 = input('Digite o nome do terceiro aluno: ')
a4 = input('Digite o nome do quarto aluno: ')
x = [a1,a2,a3,a4]
random.shuffle(x)

print('O trabalho será apresentado na seguinte ordem: {}.'.format(x,x,x,x))