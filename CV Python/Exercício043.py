print('\033[1;30mCALCULO DO IMC\n')

p = float(input('Digite sua Peso: '))
a = float(input('Digite seu Altura: '))
imc = p/a**2

print('\nSeu IMC é {:.2f}.'.format(imc))
print('ESTADO ATUAL:',end = ' ')
if imc <= 18.5:
                 print('\033[31;1mAbaixo do Peso Ideal!\nConsulte um médico.')
if imc >= 18.5 and imc <= 25:
                                print('\033[1;32mPeso Ideal!\nParabéns!')
if imc >= 25 and imc <= 30:
                             print('\033[1;33mSobrepeso!\nFique atento e comece a se cuidar!')
if imc >= 30 and imc <= 40:
                             print('\033[1;35mObesidade!\nProcure um médico!')
if imc >40:
            print('\033[1;31mObesidade Mórbida!\nSua Vida Está em Risco!')

