#Desafio022

nome = input('Digite seu nome completo: ')
print('Seu Nome Maiúsculo: {}'.format(nome.upper()))
print('Seu Nome Minúsculo: {}'.format(nome.lower()))
n = nome.split()
print('A Quantidade de Letras do Seu Nome: {}'.format(len(''.join(n))))#**
print('A quantidade de letras do seu 1º nome: {}'.format(len(n[0])))#**



#1º solução
#n2 = ''.join(n)
#n3 = (n[0])
#print('A quantidade de letras do seu nome: {}'.format(len(n2)))
#print('A quantidade de letras do seu 1º nome: {}'.format(len(n3)))
# implementação 2º Solução**