from math import log10,e,pi

a = float(input()) 
b = float(input())
c = float(input())
d = float(input())

resultado = (a**2 + 3 * b)/c+d


print("i)", round(resultado, 4))


resultado = log10(a)+e**(-b/c)-d**2/pi


print("ii)", round(resultado, 4))

# a lado do cubo de volume a² = a ** (1/3) * a ** (1/3) 
# o volume do cubo de volume a = a ** (1/3) * a ** (1/3) ** a ** (1/3) 

resultado = (a**(2/3)*b**(1/3)+c*d)/(a+b+c+d)


print("iii)", round(resultado, 4))



resultado = (a+b)*(c+d)/(a*b*c*d)


print("iv)", round(resultado, 4))


resultado = ((a**2 + b**2) / (c*d)) - ((c**2 + d**2) / (a*b))


print("v)", round(resultado, 4))


resultado = (a+b+c+d)**2


print("vi)", round(resultado, 4))


resultado = (a**2)+(b**2)+(c**2)+(d**2)


print("vii)", round(resultado, 4))



resultado = (a*b*c*d)**(1/3)
##o lado do cubo de volume (produto de a,b,c,d)  = x**1/3

print("viii)", round(resultado, 4))
