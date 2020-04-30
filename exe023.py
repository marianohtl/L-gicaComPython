# F! Fatorial

n = int(input('Digite o valor de n: '))
i = n
f = n
while i > 0:
    i = i - 1
    if i > 1:
        f = f * i

if n == 0:
    print(1)
else:
    print(f)