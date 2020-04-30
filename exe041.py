#Desafio034

s = float(input('Digite o valor do salário do funcionário: R$ '))
if s > 1250.00:
    a = s*1.1
    print('Você ganhou um aumento de 10%, seu salário atual é {:.2f}.'.format(a))
else:
    a=s*1.15
    print('Você ganhou um aumento de 15%, seu salário atual é {:.2f}.'.format(a))