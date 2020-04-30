#Desafio022 - Aula

nome = str(input('Digite seu nome completo: ')).strip() #usando a função .strip (espaços antes e depois erradicados)
print('Analizando seu nome ...')
print('Seu nome em maiúsulas é {}'.format(nome.upper()))
print('Seu nome me minúsculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))  # MUITO LEGAL >> - QUANTIDADE DE ESPAÇOS EM BRANCO
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))#vai dar a posição do primeiro espaço <0 , 1 , 2 , 3 > -Quantidade de Letras-

# outra maneira
# separa = nome.split
# print('Seu primeiro nome é {} e ele tem {} letras.'.format(separa[0], len(separa[0])))
