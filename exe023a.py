import math

ângulo = float(input('Digite o angulo que você deseja: '))
seno = math.sin(math.radians(ângulo)) # converte o ângulo digitado para radianos e calcula o seno
print('O ângulo de {} tem o SENO de {:.2f}.'.format(ângulo,seno))
cosseno = math.cos(math.radians(ângulo)) # converte o ângulo digitado para radianos e calcula o cosseno
print('O ângulo de {} tem o COSSENO de {:.2}.'.format(ângulo,cosseno))
tangente = math.tan(math.radians(ângulo)) # converte o ângulo digitado para radianos e calcula o tangente
print('O ângulo de {} tem a Teangente de {:.2}.'.format(ângulo, tangente))

# possível usar apenas seno / cosseno / tangente
