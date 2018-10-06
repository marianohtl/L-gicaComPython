print('\033[1;30m-'*40)
print('             MÉDIA ESCOLAR')
print('-'*40)

n = float(input('1º NOTA: '))
n2 = float(input('2º NOTA: '))

m = (n+n2)/2

print('\nSITUAÇÃO DO ALUNO:',end=' ')
if m < 5:
        print('\033[31;1mREPROVADO!')
elif m >= 5.0 and m <= 6.9:
                         print('\033[1;33mRECUPERAÇÃO!')
elif m > 7.0:
             print('\033[32;1mAPROVADO!')