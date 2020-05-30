# n = [int(num) for num in input().split()]
pares = [int(num) for num in input().split()]

listaAlunos = []
for n in range(1,pares[0] +1):
  listaAlunos.append(input().lower())

lista_ordenada = sorted(listaAlunos)
print(lista_ordenada[pares[1] -1])
