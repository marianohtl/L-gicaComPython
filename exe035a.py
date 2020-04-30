# Desafio.028

from random import randint
from time import sleep  # ou biblioteca time
computador = randint(0, 5) # faz o computador "pensar"
print('-=-'*20)
print(' Vou pensar em um número entre 0 e 5. Tente adivinhar ...')
print('-=-'*20)
jogador = int(input('Em que número pensei? ')) # Jogador tenta advinhar
print('Processando...')
sleep(3) # faz o computador "dormir por x(3) segundos ..."
if jogador == computador:
    print('Parabéns! Você conseguiu me vencer!')
else:
    print('Ganhei! Eu pensei no número {} e não no número {}!'.format(computador, jogador))
