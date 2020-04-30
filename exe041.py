# Exercício 1 - UM QUADRADO PREENCHIDO COM #  - Semana 7

l = int(input('digite a largura: '))
a = int(input('digite a altura: '))


ii = 1
while ii <= a:
    i = 1
    while i <= l:
        print('#', end='')
        i = i + 1
    print()
    ii = ii + 1