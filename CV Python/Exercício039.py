from datetime import date

print('\033[1;32m-'*40)
print('           ALISTAMENTO MILITAR')
print('-'*40)
ano = int(input('\033[1;30mDigite o ano do seu nascimento: '))
idade = date.today().year - ano

if idade < 18:
              f = 18 - idade
              print('\n\033[1;36MVocê ainda não alcançou a idade para o alistamento!')
              print('Falta(m) {} ano(s) para que você possa se alistar.'.format(f))
elif idade > 18:
                f = idade - 18
                print('\n\033[1;31mVocê excedeu a idade limite para o alistamento.')
                print('Tens que pagar multa devido ao(s) {} ano(s) de atraso!'.format(f))
elif idade == 18:
                print('\n\033[1;32mEstá na idade certa para se alistar!')
