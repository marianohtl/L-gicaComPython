#Desafio023
# erro com números menores que 1000
num = int(input('Digite um número: '))
n = str(num)
print('Analizando o número {} ... '.format(num))
print('Unidade: {}'.format(n[3]))
print('Dezena: {}'.format(n[2]))
print('Centena: {}'.format(n[1]))
print('Milhar: {}'.format(n[0]))

nuum = int(input('Digite um número: '))
u = nuum // 1 % 10
d = nuum // 10 % 10
c = nuum // 100 % 10
m = num // 1000 % 10
print('Unidade:',(u))
print('Dezena:',(d))
print('Centena:',(c))
print('Milhar:',(m))

#print('Analizando o número {} ... '.format(nuum))
#print('Unidade: {}'.format())
#print('Dezena: {}'.format())
#print('Centena: {}'.format())
#print('Milhar: {}'.format())


