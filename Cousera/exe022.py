#Números Adjacentes Iguais
sequência = input('Digite uma Sequência Numérica: ')
indiPassag = True
i = 0
comprimento = int(len(sequência))
n1 = 0
n2 = 0
a = 0
while indiPassag == True:
    if i < comprimento:
        n1 = sequência[i]
        i = i+1
        if n1 == n2:
            print('Na sequência {}, o número {} é um número adjacente igual.'.format(sequência,n1))
            a = a + 1
        else:
            n2 = n1
    else:
        if a == 0:
            print('Não há números adjacentes iguais na sequência informada.')
            indiPassag = False
        else:
            indiPasag = False
