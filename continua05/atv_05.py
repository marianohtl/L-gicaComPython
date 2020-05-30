n = input()
lista = []

def somaNum(n):
  soma = 0
  for i,numero in enumerate(n):
     lista.append(int(numero))
     soma+= lista[i]
  print(soma)


somaNum(n)