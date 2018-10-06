#Desafio.029

v = int(input('Qual é a velocidade, em km/h, que seu carro se encontra?\n'))
if v>80:
    s = float((v - 80)*7)
    print('Está acima da velocidade permitida neste percurso.\n'
          'Irá receber uma multa de R${:.2f}!'.format(s))
else:
    print('Continue a nadar! =) ')