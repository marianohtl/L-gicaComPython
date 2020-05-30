from math import ceil,floor
## Cada litro cobre 7 metros quadrados
## area = em metros quadrados
## litrosNecessarios = area / 7 
## litrosNecessarios / 24
## litrosNecessarios / 5.4
## litrosNecessarios / 24 &&  resto = litrosNecessarios % 24  && litrosNecessarios / 5.4

area = float(input())

litrosNecessarios = area / 7 

maiorLata =  ceil(litrosNecessarios / 24)
precoFinal = 91 * maiorLata
print("a)",maiorLata,"lata(s) de 24 litros: R$ {:.2f}".format(precoFinal))
 
menorLata = ceil(litrosNecessarios / 5.4)
precoFinal = 23.00 * menorLata
print("b)",menorLata,"lata(s) de 5.4 litros: R$ {:.2f}".format(precoFinal))

maiorLata = floor(litrosNecessarios/24)
resto = litrosNecessarios % 24
menorLata = ceil(resto / 5.4)

precoFinal = menorLata * 23 + maiorLata * 91
print("c)",maiorLata,"lata(s) de 24 litros e",menorLata,"lata(s) de 5.4 litros: R$ {:.2f}".format(precoFinal))
