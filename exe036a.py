#Desafio.029

#Refinamento Sucessivo <<DIVIDIR PARA CONQUISTAR>> resolver as tarefas aos poucos

velocidade = float(input('Qua é a velocidade atual do carro? '))
if velocidade > 80:                 #Condição Simples
    print('Multado! Você excedeu o limite permitido que é de 80Km/h.')
    multa = (velocidade-80) * 7
    print('Você deve pagar uma multa de R${:.2f}'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')

