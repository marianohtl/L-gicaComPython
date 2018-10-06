#Conversor de Segundos

s = int(input('Por favor, entre com o número de segundos que deseja converter: '))
a = s // 86400 #dias
md = s % 86400 #módulo dias
b = md // 3600 #horas
mh = md % 3600  #módulo horas
c = mh // 60 #minutos
d = mh % 60 #módulo de minutos == seu


print('{} dias, {} horas, {} minutos e {} segundos.'.format(a,b,c,d))