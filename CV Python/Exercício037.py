print('\033[7m=\033[m'*37)
print('\033[7m      Conversão de Bases Numéricas   \033[m')
print('\033[7m=\033[m'*37)
n = int(input('\033[1mDigite um Número: '))
print('\033[1m-'*37)
print('')
print('\033[1;31m[1] BINÁRIA\033[m ')
print('\033[1;31m[2] OCTAL\033[m')
print('\033[1;31m[3] HEXADECIMAL\033[m')
print('')
r = int(input('\033[1mSELECIONE A BASE NUMÉRICA DESEJADA:'))
print('-'*37)

b = bin(n)[2:]
o = oct(n)[2:]
h = hex(n)[2:]

if r == 1:
            print('\033[1;31m{} na base 2'.format(b))
elif r == 2:
            print('\033[1;31m{} na base 8'.format(o))
elif r == 3:
            print('\033[1;31m{} na base 16'.format(h))
