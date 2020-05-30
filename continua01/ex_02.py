from math import log,e,pi

n = float(input())
resultado = n**2
print("i)", resultado)

resultado = n ** e 
print("ii)",resultado)

resultado = n**(1/2)
print("iii)",resultado)

resultado = n**(1/3)
print("iv)",resultado)

resultado = n **(1/n)
print("v)", resultado)

resultado = e*n
print("vi)",resultado)

resultado = pi /n
print("vii)",resultado)

resultado =  log(n,7)
print("viii)",resultado)

resultado =  log(n,e)
print("ix)",resultado)

resultado =  log(n,pi)
print("x)",resultado)
