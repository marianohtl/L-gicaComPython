def num_digitos(n):
  total =1
  while n // 10 != 0:
    n = n // 10
    total = total + 1
  return print(total)

n = int(input())
num_digitos(n)