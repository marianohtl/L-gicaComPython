# Soma dos Algarismos
n = input('Digite um número inteiro: ')
i = len(n)
n = int(n)
d = 1
dd = 1
soma = 0
while i >= 0:
    d = d * 10
    n1 = n % d
    n2 = n1 // dd
    dd = dd * 10
    soma = soma + n2
    i = i - 1

print(soma)