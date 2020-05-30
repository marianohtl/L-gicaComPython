lista = [int(num) for num in input().split()]

def listaInteiros(lista=[]):
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
      for numeros in lista:
        print(numeros, end=" ")
    if comand[0] == "final":
      lista.sort()
      for numeros in lista:
        print(numeros, end=" ")
        end = "end"

listaInteiros(lista)
