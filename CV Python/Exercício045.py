from random import randint
from time import sleep

print('\033[1;30m-=-\033[m'*10)
print('\033[1;30mSuas opções: ')
print('\033[36;1m[1] PEDRA')
print('\033[33;1m[2] PAPEL')
print('\033[35;1m[3] TESOURA')
print('\033[1;30m-=-\033[m'*10)
x = int(input('\033[1;30mQual é a sua jogada? '))
print('\033[30;1m-=-\033[m'*10)
y = randint(1,3)
if x == 1:
          xl = 'Pedra'
elif x == 2:
            xl = 'Papel'
elif x == 3:
            xl = 'Tesoura'

if y == 1:
          yl = 'Pedra'
elif y == 2:
            yl = 'Papel'
elif y == 3:
            yl = 'Tesoura'


sleep(1)
print('\033[36;1mJO')
sleep(1)
print('\033[33;1mKEN')
sleep(1)
print('\033[35;1mPÔ\033[m')
sleep(0.4)
print('\033[30;1m-=-\033[m'*10)
print('\033[1;31mComputador jogou {}.\033[m'.format(yl))
print('\033[1;32mJogador jogou {}.\033[m'.format(xl))
print('\033[30;1m-=-\033[m'*10)

if x == y:
            print('\033[33;1mHouve um Empate!\033[m')
elif x == 1 and y == 2:
                          print('\033[1;31mComputador Vence!\033[m')
elif x == 1 and y == 3:
                          print('\033[1;32mJogador Vence!\033[m')
elif x == 2 and y == 1:
                          print('\033[1;32mJogador Vence!\033[m')
elif x == 2 and y == 3:
                          print('\033[1;31mComputador Vence!\033[m')
elif x == 3 and y == 1:
                          print('\033[1;31mComputador Vence!\033[m')
elif x == 3 and y == 2:
                          print('\033[1;32mJogador Vence!\033[m')