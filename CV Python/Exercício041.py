#Enunciado Mudou na Resolução do Exercício
from datetime import date
print('\033[1;30m='*50)
print('         CONFEDERAÇÃO NACIONAL DE NATAÇÃO')
print('='*50)
nasc = int(input('\nDigite o ano do seu nascimento: '))
idade = date.today().year-nasc

print('CATEGORIA:',end = ' ')
if idade > 0 and idade <= 9:
                            print('\033[36;1mMIRIM')
elif idade > 9 and idade <=14:
                                 print('\033[1;34mIFANTIL')
elif idade > 14 and idade <=19:
                                  print('\033[1;33mJÚNIOR')
elif idade > 19 and idade <=20:
                                 print('\033[1;35mSÊNIOR')
elif idade > 20:
                print('\033[1;31mMASTER')

