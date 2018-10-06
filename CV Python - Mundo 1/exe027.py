# Aula 09 Manipulando Strings  - RESUMÃÃÃO
# completo

frase = 'Curso em Vídeo Python'
print(frase) #frase em minisespasços dentro da memória do pc , iniciando com 0
print(frase[3])  # imprime a quarta letra [0,1,2,3]
print(frase[3:13]) # imprime da quarta letra até a letra 13º letra [4º <s>,5º <o> ... 11º <d>, 12º <e>, 13º STOP]
print(frase[1:15])
print(frase[::2])#:: sem início e sem final (string toda), pulando em passo 2
print(frase[15:])#indico o início porém não temos o final = até o final da string
print(frase[9::3])#d começa no 9 , até o fim , no passo 3

print('\n')
print('TEXTO LONGO\n')

print('''Gatos são majestosos por excelência.
Quando filhotes, são ainda mais apaixonantes. 
Para quem está pensando em adquirir um bebê 
felino, é importante saber que eles têm exigências 
diferentes dos adultos.\n''')
# textos longos com ''' < ou """

print(frase.count('o'))# conta quantas vezes tem a letra o
print(frase.count('O'))
print(frase.count('o',0,13))# contagem de "o", já com o fatiamento da string <0 até 13> -
print(frase.upper().count("O"))# transforma a frase em letras maiúsculas e conta a quantidade de O
print(len(frase))# Quantidade de Caracteres
frase2 = "  Curso em Vídeo Python   "
print(len(frase2)) #  Quantidade de Caracteres - 'conta os espaços'
print(len(frase2.strip())) #tira os espaços em branco que estão antes e depois da string, e conta seus caracteres
print(frase2.replace('Python', 'Android')) # troca os python por android
print(frase[0])# uma string é imutável , frase[0] = j  <Error>

# nesta sequência , apenas em uma instância existe a substituição, não diretamente na variável
base = 'Curso em Vídeo Python'
base.replace('Python', 'Android')
print(base)
# diferente, pois base recebeu base.replace()
base = 'Curso em Vídeo Python'
base = base.replace('Python', 'Android')
print(base)

print('Curso' in frase) #verifica se tal palavra está dentro da frase True or False <in operador>
print(frase.find('Curso'))#mostra a posição em que a string curso se encontra <0>
print(frase.find('Vídeo'))# vídeo está na posição 9
print(frase.find('vídeo'))# não existe , então mostra a posição -1
print(frase.lower().find('vídeo'))# transforma a string em letras minúsculas e procura a posição de vídeo
print(frase.split())# cria uma lista dividindo a frase ['Curso' 'em' 'vídeo' 'Python']
dividido = frase.split()
print('-'.join(dividido))#com nomes separados em listas, usamos join para juntar uma coisa na outra, neste caso irá juntar a lista com o >> - <<

print(dividido)
print(dividido[0])
print(dividido[3]) # mostra a 3 palavra do split
print(dividido[3][0]) # mostra a primeira letra <0> da 3º palavra de Python
print(frase.upper())#método , significa pra cima ,vai ficar em maipusculas
print(frase.lower())# o contrário de uper <tudo em minúsculo>
print(frase.capitalize())#capitalize - todos para minúsculo e a primeira letra se tornará maiúscula
print(frase.title())#title - irá fazer uma análize de quantas palavras tem baseando-se nos espaços, transformanção início maiusc, palavra apor palavra
print(len(frase2.strip())) #tira os espaços em branco que estão antes e depois da string, e conta seus caracteres
print(frase2.strip()) #tira os espaços em branco que estão antes e depois da string
print(frase2.rstrip()) # remove os últimos espaços (ditreita <r>)
print(frase2.lstrip()) # remove os espaços do início (esquerda <l>)
print(len(frase2.rstrip()))#remove espaços da direita e conta a quantidade de caracteres
print(len(frase2.lstrip()))#remove os espaços da esquerda e conta a quantidade de caracteres

#escrevendo um nome ao contrário
nome = input('Digite seu nome: ' )
print(nome[::-1])
#escrevendo uma lista ao contrário
nome = input('Digite uma lista com dez ítens: ')
lista = nome.split()
lista2 = lista[::-1]
print(lista2)

nome = str(input('Digite seu nome completo: ')).strip() #usando a função .strip (espaços antes e depois erradicados)
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))  # MUITO LEGAL >> - QUANTIDADE DE ESPAÇOS EM BRANCO
