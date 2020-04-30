print('\033[30;1m-'*40)
print('        CLASSIFICANDO TRIÂNGULOS')
print('-'*40)

print('Diga as Medidas do Seu Triângulo:')
l1 = int(input('1º LADO: '))
l2 = int(input('2º LADO: '))
l3 = int(input('3º LADO: '))

if l1+l2 > l3 and l2+l3 > l1 and l3+l1 > l2:
                                            c = 1
                                            print('\033[32;1mOlha um Triângulo!')
else:
    c = 0
    print('\033[31;1mNão temos um triângulo!')

if c == 0:
          print('#chateada =( ')
elif l1 == l2 and l2 == l3 and l1 == l3:
                                        print('Esse Triângulo é Equilátero!')
elif l1 == l2 or l2 == l3 or l3 == l1:
                                      print('Esse Triângulo é Isósceles!')
elif l1 != l2 and l2 != l3 and l1 != l3:
                                        print('Esse Triângulo é Escaleno!')


