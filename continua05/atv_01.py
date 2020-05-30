listaAno = [int(ano) for ano in input().split()]

def contaDigitos(listaAno):
  quantidadeDigitos = []
  for ano in listaAno:
    total =1
    while ano // 10 != 0:
      ano = ano // 10
      total = total + 1
    quantidadeDigitos.append(total)

  return quantidadeDigitos

quantidadesDigitos = contaDigitos(listaAno)

def ehBissexto(listaAno):
  bissexto = []
  for ano in listaAno:
    if ano % 4 == 0 and ano % 100 != 0 or ano%400 == 0 :
      bissexto.append(True)
    else:
        bissexto.append(False)
  return bissexto

def Mensagem(quantidadeDigitos, bissexto, listaAno):
  for i, digito in enumerate(quantidadeDigitos):
    if digito <4:
      print("Ano invalido")
    else:
      if bissexto[i] == False:
        print(f"O ano {listaAno[i]} NAO eh bissexto")
      else:
        if listaAno[i] >= 2020:
          print(f"O ano {listaAno[i]} serah bissexto")
        elif listaAno[i] >= 0 and listaAno[i] < 2020:
          print(f"O ano {listaAno[i]} foi bissexto")

quantidadeDigitos = contaDigitos(listaAno)
bissexto = ehBissexto(listaAno)

Mensagem(quantidadeDigitos, bissexto, listaAno)