#desafio019

#import random <random.choice()>
from random import choice
print('='*25)
print ('   Sorteio dos Alunos')
print('='*25)

a1 = input('Nome do 1º aluno:')
a2 = input('Nome do 2º aluno:')
a3 = input('Nome do 3º aluno:')
a4 = input('Nome do 4º aluno:')
t = (a1,a2,a3,a4)
s = choice(t)

print ('O aluno sorteado para limpar o quadro será {}.'.format(s))
