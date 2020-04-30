# Desafio.028

print('-'*30)
print('      Jogo da Adivinhação')
print('-'*30)

import random
n = random.randint(0,5)
u = int(input(' De 0 a 5, adivinhe que número estou pensando...\n >>> '))
if u == n:
    print(' O número que pensei foi {}.'.format(n))
    print(' Você Venceu! Grrr')
else:
    print(' O número que pensei foi {}.'.format(n))
    print(' Você Perdeu! HaHaHa')