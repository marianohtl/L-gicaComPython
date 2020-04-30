#desafio027

n = str(input('Digite seu nome completo: ')).strip()# elimina espaços
nome = n.split() #lista
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}'. format(nome[0]))
print('Seu último nome é {}'.format(nome[len(nome)-1]))# tamanho da lista - 1,2,3,4... -1, pois a posição de contagem começa do 0
