import math

listaCompras = []
i = 0
Compras = [compra for compra in input().split()]
listaCompras.append(Compras)
listaProdMaiorPreco = listaCompras

while listaCompras[i] != ["0","0","0"]:
  Compras = [compra for compra in input().split()]
  listaCompras.append(Compras)
  i+= 1

contador = 0
preco = 0.0
quantidade = 0
codigo = ""
precoAnterior = 0.0
codigoMaior = ""
quantidadeProd = 0
precoMaior = 0.0

for i, compras in enumerate(listaCompras):
    contador = 1
    for dados in listaCompras[i]:
      if contador == 1:
        codigo = dados
      elif contador == 2:
        quantidade = int(dados)
      elif contador == 3:
        preco = float(dados)

      contador += 1
    precoMaior = float(preco * quantidade)
    if precoMaior > precoAnterior:
      precoAnterior = precoMaior
      quantidadeProd = quantidade
      codigoMaior = codigo
      listaProdMaiorPreco = [codigoMaior, quantidadeProd, precoAnterior]

if listaProdMaiorPreco[0] == ["0","0","0"]:
  print("nao tem compras")
else:
  print("Item mais caro")
  for i, dadosLista in enumerate(listaProdMaiorPreco):
      if i == 0:
        print(f"Codigo: {dadosLista}")
      if i == 1:
        print(f"Quantidade: {dadosLista}")
      if i == 2:
        print(f"Custo: {math.ceil(dadosLista * 100)/100:.2f}")
