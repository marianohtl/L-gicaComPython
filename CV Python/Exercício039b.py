from datetime import date

sexo = input('\033[1;30mDIGITE O SEU GÊNERO: ').strip()
sexo = sexo.upper()
if sexo == 'FEMININO':
    print('SITUAÇÃO ATUAL: \033[1;32mREGULARIZADA\n'
          '\033[1;30Mulheres são isentas do alistamento militar.')
elif sexo == 'MASCULINO':
    ano = int(input('DIGITE O ANO DO SEU NASCIMENTO: '))
    hoje = date.today().year
    idade = hoje - ano
    print('Quem nasceu em {} tem {} em {}'.format(ano,idade,hoje))
    if idade < 18:
        falta = 18 - idade
        print('SITUAÇÃO ATUAL: \033[1;32mREGULARIZADA\n'
              '\033[1;30mFaltam {} ano(s) para você se alistar.'.format(falta))
    elif idade > 18:
        falta = idade - 18
        alistamento = hoje - idade
        print('SITUAÇÃO ATUAL: \033[1;31mDESREGULARIZADA\n'
              '\033[1;30mUltrapassaram {} ano(s) do seu alistamento.'.format(falta))
        print('Seu alistamento foi em {}.'.format(alistamento))
    else:
        print('SITUAÇÃO ATUAL: \033[1;36mPENDENTE')
        print('\033[30mVocê deve se alistar \033[1;30mIMEDIATAMENTE!')
else:
    print('\033[1;31mGÊNERO INVÁLIDO!')