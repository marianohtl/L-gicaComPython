r1 = float(input('Primeiro seguimento: '))
r2 = float(input('Segundo seguimento: '))
r3 = float(input('Terceiro seguimento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os seguimentos acima PODEM FORMAR um triângulo', end = ' ')
    if r1 == r2 == r3:                    #if r1 == r2 and r2 == r3
        print('EQUILÁTERO!')
    elif r1 != r2 != r3 != r1:            #if r1 != r2 and r2 != r3 and r2 != r3:
        print('ESCALENO!')
    else:
        print('ISÓCELES!')
else:
    print('Os seguimentos acima NÃO PODEM FORMAR triângulo!')