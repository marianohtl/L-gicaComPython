#desafio026

frase = str(input('Digite uma frase: ')).strip()
frasee = frase.lower()
n = len(frasee)
print('Nessa frase temos {} vezes a letra a.'.format(frasee.count("a")))
print('A primeira letra a se localiza na posição :',frasee.find('a')+1)
print('A última letra "a" está na posição: ', frasee.rfind('a')+1)
#solucionei com os exercícios

