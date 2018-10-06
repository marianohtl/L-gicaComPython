# SEMANA 6 - Jogo do NIM - COM BUGS

def campeonato():
    print('**** Rodada 1 ****\n')
    partida()
    print('\n**** Rodada 2 ****\n')
    partida()
    print('\n**** Rodada 3 ****\n')
    partida()
    print('\n*** Final do campeonato! ***\n')
    placar = 'Placar: Você 0 X 3 Computador'
    return placar


def usuario_escolhe_jogada(x,y):
    z = 1
    while z != 0:
        j = 'a'
        while j.isnumeric() != True:
            j = input('\nQuantas peças você vai querer tirar? ')
            if j.isnumeric() != True:
                print('\nOops! Jogada inválida! Tente de novo.')

        j = int(j)
        print('')
        if j <= y:
            z = 0
        else:
            z = 1
            print('\nOops! Jogada inválida! Tente de novo.')

    return j


def computador_escolhe_jogada(x,y):
    trap = y + 1
    if x % trap <= y:
        jpc = x % trap
    elif x % trap == 0:
        jpc = y

    return jpc


def partida():
    n = 'a'
    while n.isnumeric() != True:
        n = input('Quantas peças? ')
        if n.isnumeric() != True:
            print('\nOops! Jogada inválida! Tente de novo.')

    m = 'a'
    while m.isnumeric() != True:
        m = input('Limite de peças por jogada? ')
        if m.isnumeric() != True:
            print('\nOops! Jogada inválida! Tente de novo.')

    m = int(m)
    n = int(n)

    if n%(m+1) == 0:
        print('\nVocê começa!\n')
        while n != 0:
            j = usuario_escolhe_jogada(n,m)
            n = n - j
            print('Você tirou {} peça(s).\nAgora resta apenas {} peça(s) no tabuleiro.\n'.format(j, n))
            pc = computador_escolhe_jogada(n,m)
            n = n - pc
            print('Computador tirou {} peça(s).\nAgora resta apenas {} peça(s) no tabuleiro.\n'.format(pc, n))
        print('Fim do jogo! O computador ganhou!')
    else:
        while n != 0:
            print('\nComputador começa!\n')
            pc = computador_escolhe_jogada(n,m)
            n = n - pc
            print('Computador tirou {} peça(s).\nAgora resta apenas {} peça(s) no tabuleiro.\n'.format(pc,n))
            if n > 0:
                j = usuario_escolhe_jogada(n,m)
                n = n - j
                print('Você tirou {} peça(s).\nAgora resta apenas {} peça(s) no tabuleiro.\n'.format(j, n))
        print('Fim do jogo! O computador ganhou!')


def main():
    e = 'a'
    while e.isnumeric() != True:
        e = input('\nBem-vindo ao jogo do NIM! Escolha: \n\n'    
            '1 - para jogar a partida isolada\n'
            '2 - para jogar um campeonato   ')

        if e.isnumeric() != True:
            print('\nOops! Jogada inválida! Tente de novo.')

    return e

e = int(main())
passag = True
while passag == True:
    if e != 1 and e != 2:
        while e != 1 and e != 2:
            e = int(main())
            print('\nOops! Jogada inválida! Tente de novo.')
    elif e == 1:
        print('\nVocê escolheu uma partida isolada!\n')
        partida()
        passag = False
    else:
        print('\nVocê escolheu campeonato!\n')
        print(campeonato())
        passag = False