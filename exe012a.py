#desafio08

m = float(input('Digite a quantidade de metros: '))
km = m/1000
hm = m/100
dam = m/10
dm = m*10
cm = m*100
mm = m*100

print('A medida {} metros corresponde a: '.format(m))
print(' {}km\n {}hm\n {}dam\n {}dm\n {}cm\n {}mm'.format(km,hm,dam,dm,cm,mm))
