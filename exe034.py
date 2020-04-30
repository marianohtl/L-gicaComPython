# Aula 10

# ESTRUTURA CONDICIONAL SIMPLES
nome = str(input('Qual é o seu nome? '))
if nome == 'Gustavo':
    print('Que nome lindo você tem!')
print('Bom dia, {}!\n'.format(nome))

#Estrutura CONDICIONAL COMPOSTA

nome = str(input('Qual é o seu nome mesmo? '))
if nome == 'Gustavo':
    print('Que nome lindo!')
else:
    print('Seu nome é tão normal!')
print('Bom dia, {}!\n'.format(nome))


'''
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1+n2)/2
print('Sua média foi {:.1f}'.format(m))
if m >= 6.8:
    print('Sua média foi boa! PARABÉNS!')
else:
    print('Sua média foi ruim! ESTUDE MAIS!')'''


#CONDIÇÃO SIMPLIFICADA

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print('Sua média foi {}'.format(m))
print('PARABÉNS!' if m>=6 else "Estude Mais!")