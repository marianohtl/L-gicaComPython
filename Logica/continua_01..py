print("Digite a quantidade de nomes que tu vai digitar:")
n = int(input())

while n<=3  or n >=10:
  if n<=3:
    print("A quantidade de nomes deve ser maior que 3.")
    print("Digite a quantidade de nomes que tu vai digitar:")
    n = int(input())
  elif n >= 10 :
    print("A quantidade de nomes deve ser menor que 10.")
    print("Digite a quantidade de nomes que tu vai digitar:")
    n = int(input())

l = [None] * n
i = 0
while i <= len(l) - 1:
    print("Digite um nome:")
    l[i] = input()
    i = i +1

l.insert(3,"Teste")
l.pop(2)

i = 0
for nomes in l:
   if nomes == "Ana":
     i = i +1

print(f"Quantidade de vezes que o nome Ana se repete: {i}")

if i > 0:
  for i in range(n):
      if l[i] == 'Ana':
          print(f"O índice da primeira ocorrência de Ana na lista l é {i}")
          break
  i = 0


l = sorted(l)
print(l)
