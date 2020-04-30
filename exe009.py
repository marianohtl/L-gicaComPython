#desafio005
print('--'*25)
print('             ANTECESSOR E SUCESSOR')
print('--'*25)
num = int(input('Escolha um número: '))
s = num+1
sub = num-1
print('{} {} {}'.format(sub,num,s))
print('O antecessor de {} é {}.'.format((num),(sub)))
print('O sucessor de {} é {}.'.format((num),(s)))
