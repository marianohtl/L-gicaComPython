#Desafio031


d = int(input('Qual será a distância da sua viagem, em Km\H? '))
if d <= 200:
    v = d*0.5
    print('Sua passagem irá custar R$ {:.2f}'.format(v))
else:
    v = d*0.45
    print('Sua passagem irá custar R$ {:.2f}'.format(v))
print('Boa Viagem!')
