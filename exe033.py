#desafio027

print('Olá, eu sou o Computador!')  # não posso usar método
nome = input('Qual é o seu nome completo? ')
lista = nome.split()
lista2 = lista[::-1]
print('Prazer em te conhecer, {} {}!'.format(lista[0],lista2[0]))



nome = str(input('Qual o seu nome completo? ')).split() # posso usar método graças a str
nomee = nome[::-1]
print('Prazer em te conhecer, {} {} !'.format(nome[0],nomee[0]))