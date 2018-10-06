print('\033[1;30m-----------------------------------------------------')
print('                SIMULAÇÃO DE VENDAS')
print('-----------------------------------------------------')
preço = float(input('PREÇO: R$'))
print('-----------------------------------------------------\n'
      '             CONDIÇÕES DE PAGAMENTO\n'
      '-----------------------------------------------------'
      '\033[1;33m\n[1] À VISTA: DINHEIRO OU CHEQUE 10% DE DESCONTO\n'
      '[2] À VISTA NO CARTÃO: 5% DE DESCONTO \n'
      '[3] EM ATÉ 2X NO CARTÃO: PREÇO NORMAL\n'
      '[4] 3X OU MAIS NO CARTÃO: 20% DE JUROS\033[m\n'
      '\033[1;30m-----------------------------------------------------')

pag = int(input('DIGITE A FORMA DE PAGAMENTO:'))
print('-----------------------------------------------------')
p1 = preço - preço*0.1
desc1 = preço*0.1
p2 = preço - preço*0.05
desc2 = preço*0.05
p4 = preço + preço*0.2
juros = preço*0.2

if pag == 1:
            print('FORMA DE PAGAMENTO: À VISTA / EM CHEQUE\n'
                  'CUSTO DO PRODUTO: R${:.2f}\n'
                  '\033[1;32mDESCONTO: R${:.2f}\n\033[m\033[1;30m'
                  'TOTAL A PAGAR: R${:.2f}'.format(preço,desc1,p1))
elif pag == 2:
              print('FORMA DE PAGAMENTO: À VISTA NO CARTÃO\n'
                    'CUSTO DO PRODUTO: R${:.2f} \n'
                    '\033[1;32mDESCONTO: R${:.2f} \n\033[m\033[1;30m'
                    'TOTAL A PAGAR: R${:.2f} \n'.format(preço,desc2,p2))
elif pag == 3:
              p = int(input('DESEJA PARCELAR? Sim [1]/ Não[2] '))
              print('-----------------------------------------------------')
              if p == 1:
                        par = preço/2
                        print('FORMA DE PAGAMENTO: EM ATÉ 2X NO CARTÃO\n'
                        'CUSTO DO PRODUTO: R${:.2f} \n'
                        '\033[1;32mDESCONTO: R$00,00\n\033[m\033[1;30m'
                        'TOTAL A PAGAR: R${:.2f}\n'
                        '2X DE: R${:.2f} \n'.format(preço,preço,par))
              else:
                   par = preço / 2
                   print('FORMA DE PAGAMENTO: EM ATÉ 2X NO CARTÃO\n'
                         'CUSTO DO PRODUTO: R${:.2f} \n'
                         '\033[1;32mDESCONTO: R$00,00\n\033[m\033[1;30m'
                         'TOTAL A PAGAR: R${:.2f}\n'
                         '1X DE: R${:.2f} \n'.format(preço,preço, preço))
elif pag == 4:
              p = int(input('DESEJA PARCELAR EM MAIS DE 3 PARCELAS? Sim[1]/Não[2] '))
              print('-----------------------------------------------------')
              if p == 1:
                        par = int(input('QUANTAS SERÃO AS PARCELAS?'))
                        print('-----------------------------------------------------')
                        x = p4/par
                        print('FORMA DE PAGAMENTO: 3X OU MAIS NO CARTÃO\n'
                              'CUSTO DO PRODUTO: R${:.2f}\n'
                              '\033[31;1mJUROS: R${:.2f}\n\033[m\033[1;30m'
                              'TOTAL A PAGAR: R${:.2f}\n'
                              '{}X DE R${:.2f}\n'.format(preço,juros,p4,par,x))
              else:
                   x = p4/3
                   print('FORMA DE PAGAMENTO: 3X OU MAIS NO CARTÃO\n'
                         'CUSTO DO PRODUTO: R${:.2f}\n'
                         '\033[31;1mJUROS: R${:.2f}\n\033[m\033[1;30m'
                         'TOTAL A PAGAR: R${:.2f}\n'
                         '3X DE R${:.2f}'.format(preço,juros,p4,x))