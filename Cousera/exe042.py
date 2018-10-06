# Exercício 2 - UM QUADRADO OCO ESTRUTURADO EM #  - Semana 7

l = int(input('digite a largura: '))
a = int(input('digite a altura: '))


i = 1
while i <= a:
    print('#',end='')
    ii = 3
    while ii <= l:
        if i == a or i == 1:
            print('#', end = '')
            ii = ii + 1
        else:
            print(' ', end='')
            ii = ii + 1
    print('#')
    i = i + 1

