#desafio004

print('---------------------------')
print('Classificando uma Entrada')
print('---------------------------')

var = input('Digite algo: ')
print('O tipo primitivo desse valor é ',type(var))
print('Só tem espaços? ',var.isspace())
print('É um número? ',var.isnumeric())
print('É alfabético?',var.isalpha())
print('É alfanumérico?',var.isalnum())
print('Está em maiúsculas?',var.isupper())
print('Está em minúsculas?',var.islower())
print('Está capitalizado?',var.istitle())
