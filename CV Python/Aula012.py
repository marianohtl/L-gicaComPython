#Estrtura Condicional Simples

nome = str(input('Qual é seu nome? '))
if nome == 'Gustavo':
    print('Que nome bonito!')
print('Tenha um bom dia {}!'.format(nome))


#Estrutura Condicional Composta

nome = str(input('Qual é seu nome? '))
if nome == 'Gustavo':
    print('Que nome bonito!')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia {}!'.format(nome))


#Estrutura Condiciona Aninhada

nome = str(input('Qual é seu nome? '))
if nome == 'Gustavo':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo:':
    print('Seu nome é bem popular no Brasil. ')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia {}!'.format(nome))


nome = str(input('Qual é seu nome? '))
if nome == 'Gustavo':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo:':
    print('Seu nome é bem popular no Brasil. ')
elif nome in "Ana Cláudia Jéssica Juliana":
    print('Belo nome feminino!')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia {}!'.format(nome))