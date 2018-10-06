#desafio12
print ('='*60)
print('       PROMOÇÃO - 5% DE DESCONTO EM QUALQUER PRODUTO')
print('='*60)


p = float(input('Qual o preço do produto: R$ '))
d = p-(p*0.05)
print('O preço do produto com desconto é R${:.2F}.'.format(d))
