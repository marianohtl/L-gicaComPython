num1 = int(input())
num2 = int(input())

validar = True
while validar == True:
  if num1 < 1 or num1 >= 10:
    print("Insira um número inicial entre 1 e 9")
    num1 = int(input())

  if num2 < 1 or num2 >= 10:
    print("Insira um número inicial entre 1 e 9")
    num2 = int(input())

  if num1 >= 1 and num1 < 10 and num2 >= 1 and num2 < 10:
    validar = False

if (num1 < num2):
  num = num1
  while num1 <= num2:
    for n in range(1,10):
      resultado = num * n
      print(f"{num} x {n} = {resultado}")
    print("")
    num = num + 1
    num1 = num1 + 1
else:
    num = num2
    while num2 <= num1:
      for n in range(1,10):
        resultado = num * n
        print(f"{num} x {n} = {resultado}")
      print("")
      num = num + 1
      num2 = num2 + 1

