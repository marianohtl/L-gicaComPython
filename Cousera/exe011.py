x = int(input('Digite a coordenada x do primeiro plano: '))
y = int(input('Digite a coordenada y do primeiro plano: '))
x1 = int(input('Digite a coordenada x do segundo plano: '))
y1 = int(input('Digite a coordenada y do segundo plano: '))

if abs(x - x1) >= 10 and abs(y - y1) >= 10:
    print('longe')
elif abs(x - x1) >= 10 and abs(y - y1) == 0:
    print('longe')
elif abs(y - y1) >= 10 and abs(x - x1) == 0:
    print('longe')
elif abs(x - x1) == 0 and abs(y - y1) == 0:
    print('perto')
else:
    print('perto')
