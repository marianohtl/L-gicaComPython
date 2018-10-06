print('\033[1;34m-=-'*20)
print('                   \033[1;36mEmpréstimo Bancário\033[m')
print('\033[1;34m-=-\033[m'*20)

imóvel = float(input('\033[1;36mVALOR DO IMÓVEL:\033[m '))
salário = float(input('\033[1;36mSALÁRIO:\033[m '))
prestação = int(input('\033[1;36mPRESTAÇÕES EM ANOS À PAGAR:\033[m '))


parcela = (imóvel/(prestação*12))
porcento = 0.3*salário

if parcela <= porcento:
    print('\033[1;32mEmpréstimo Aprovado!\033[m ')
    print('\033[32mO valor da parcela será \033[1;32mR${:.2f}\033[m \033[32mem \033[1;32m{} vezes.\033[m'.format(parcela, prestação))
else:
    print('\033[1;31mEmpréstimo Negado!\033[m')
    print('\033[31mO valor da parcela de \033[1;31mR${:.2f}\033[m \033[31mexcede \033[1;31m30%\033[m \033[31mdo seu salário!\033[m'.format(parcela, prestação))
