#Conversor de segundos

s = int(input('Por favor, entre com o número de segundos que deseja converter: '))
a = s // 86400
md = s % 86400
b = md // 3600
mh = md % 3600
c = mh // 60
d = mh % 60


print('{} dias, {} horas, {} minutos e {} segundos.'.format(a,b,c,d))