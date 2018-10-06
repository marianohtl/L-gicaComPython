#Números ímpares Com While

n = int(input('Digite o valor de n: '))
i = n*2
ii = 0
while i != 0:
    if ii % 2 == 1:
        print(ii)
        ii = ii + 1
        i = i - 1
    else:
        i = i - 1
        ii = ii + 1

