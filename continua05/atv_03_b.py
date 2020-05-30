lista = [int(num) for num in input().split()]
end = ""
while end != "end":
    comand = [comand for comand in input().split()]
    if comand[0] == "inserir":
      lista.append(int(comand[1]))
    if comand[0] == "remover":
      if int(comand[1]) in lista:
        lista.remove(int(comand[1]))
    if comand[0] == "parcial":
      lista.sort()
      print()
      for numeros in lista:
        if numeros == lista[len(lista) - 1]:
            print(numeros,end="")
        else:
            print(numeros,end=" ")
    if comand[0] == "final":
      lista.sort()
      print()
      for numeros in lista:
        print(numeros, end=" ")
        end = "end"