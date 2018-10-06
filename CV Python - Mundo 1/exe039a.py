#Desafio032
from datetime import date #módulo datetime, trabalhando com data (apenas date)

ano = int(input('Que ano quer analizar? Coloque 0 para analizar o ano atual: '))
if ano == 0:
    ano = date.today().year # analizando o ano atual do sistema independente do ano / máquina
if ano % 4 == 0 and ano % 100 != 0 or ano %400 == 0:
    print('O ano {} é BISSEXTO!'.format(ano))
else:
    print('O ano {} NÃO é BISSEXTO!'.format(ano))
