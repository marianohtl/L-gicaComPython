print('=='*20)
print('      Aluguel de Carros')
print('=='*20)

dias = float(input('Quantidade de Dias Alugados: '))
km =  float(input('Quantidade de km Rodados:'))
vldias = dias*60
vlkm = km*0.15

print('O valor aluguel do carro por {:.0f} dias é R${:.2f}.'.format(dias,vldias))
print('O valor referente a {:.2f}km rodados é R${:.2f}.'.format(km,vlkm))
print('Total a Pagar: R${:.2f}'.format(vlkm+vldias))

