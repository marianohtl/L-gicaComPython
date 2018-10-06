# SEMANA 7 - Tabuada com Laços Aninhados
linha = 1
coluna = 1
while linha <= 10:
    while coluna <= 10:
        print(linha * coluna,end='\t')
        coluna = coluna + 1
    print()
    linha = linha + 1
    coluna = 1


# VARIAÇÃO - 1
tab = 0
while tab < 10:
    tab = tab + 1
    i = 0
    while i < 10:
        i = i + 1
        print(tab,'x',i,'=',tab*i)
    print()


# VARIAÇÃO - 2
tab = 1
while tab <= 10:
    i = 1
    while i <= 10:
        print(tab, "x", i, "=", tab * i)
        i = i + 1
    print()
    tab = tab + 1
