#defsafio011
print('='*50)
print ('               Pintando uma Parede')
print('='*50)

m = float(input('Medida da Altura da Parede em Metros: '))
l = float(input('Medida da Largura da Parede em Metros: '))
m2 = m*l
t = m2/2
print ('Sua parede tem {:.2f} metros quadrados.'.format(m2))
print ('Você precisa de {:.2f} litros de tinta para pintar a sua parede.'.format(t))
