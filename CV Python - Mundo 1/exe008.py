#desafio004
#com .format(), .title() , \'
print('---------------------------')
print('Classificando uma Entrada ')
print('---------------------------')

var = input('Digite algo: ')
print('O tipo primitivo \'{}\' desse valor é '.format(var),type(var))
print('\'{}\' só tem espaços? '.format(var.title()),var.isspace())
print('\'{}\' é um número? '.format(var.title()),var.isnumeric())
print('\'{}\' é alfabético?'.format(var.title()),var.isalpha())
print('\'{}\' é alfanumérico?'.format(var.title()),var.isalnum())
print('\'{}\' está em maiúsculas?'.format(var.title()),var.isupper())
print('\'{}\' está em minúsculas?'.format(var.title()),var.islower())
print('\'{}\' está capitalizado?'.format(var.title()),var.istitle())
