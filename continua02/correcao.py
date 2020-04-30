largura = float(input("Digite a largura da mala em cm: "))
comprimento = float(input("Digite o comprimeto da mala em cm: "))
altura = float(input("Digite a altura da mala em cm: "))

if largura <= 45 and comprimento <= 56 and altura <= 25:
    print("PERMITIDA")
else:
    print("PROIBIDA")


#------------------


n = int(input())

if n % 2 == 0:
    print(("O numero eh {} e ele eh par").format(n))
else:
    print(("O numero eh {} e ele eh impar").format(n))

#--------------------


p1 = float(input())
p2 = float(input())
p3 = float(input())
presenca = float(input())


def nota(p1,p2,p3,presenca):
    p1 = p1 * 2
    p2 = p2 * 2
    p3 = p3 * 3
    presenca = int(presenca * 100)
    media = round((p1 + p2 + p3) / 7, 1)
    if presenca >= 75 and media < 4:
        print(("Frequencia: {}%").format(presenca))
        print(("Media: {}").format(media))
        print("Aluno reprovado!")
    elif presenca >= 75 and media >= 4 and media < 6:
        print(("Frequencia: {}%").format(presenca))
        print(("Media: {}").format(media))
        print("Aluno de recuperação!")
    elif presenca >= 75 and media >= 6 and media <= 9:
        print(("Frequencia: {}%").format(presenca))
        print(("Media: {}").format(media))
        print("Aluno aprovado!")
    elif presenca >= 75 and media > 9:
        print(("Frequencia: {}%").format(presenca))
        print(("Media: {}").format(media))
        print("Aluno aprovado com louvor!")
    elif presenca < 75:
        print(("Frequencia: {}%").format(presenca))
        print(("Media: {}").format(media))
        print("Aluno reprovado por faltas!")

nota(p1,p2,p3,presenca)

#########

def nota(p1,p2,p3,presenca):
    # Verificando se o usuário digitou as informações corretamente
    assert p1 >= 0 and p1 <= 10 and \
           p2 >= 0 and p2 <= 10 and \
           p3 >= 0 and p3 <= 10 and \
           presenca >= 0 and presenca <= 1, "Seu animal, digita certo"
    # Outra forma de comparar intervalos
    # Comparando intervalos entre -10 e 10
    # assert abs(p1) <= 10 and \
    #        abs(p2)  <= 10 and \
    #        abs(p3) <= 10 and \
    #        abs(presenca) <= 1
    # Calculando as notas com peso
    p1 = p1 * 2
    p2 = p2 * 2
    p3 = p3 * 3
    # Calculando a média (Nome chique == Média Aritmética Ponderada)
    media = round((p1 + p2 + p3) / 7, 1)
    # Imprimindo a frequência e média do aluno
    print(("Frequencia: {:.0f%}").format(presenca))  # Formatação de porcentagem no python
    print(("Media: {}").format(media))
    # Verificando a situação do aluno
    if presenca < 75:
        print("Aluno reprovado por faltas!")
    elif media < 4:
        print("Aluno reprovado!")
    elif media < 6:
        print("Aluno de recuperação!")
    elif media <= 9:
        print("Aluno aprovado!")
    else:
        print("Aluno aprovado com louvor!")



salario = float(input())

if salario <= 1751.81:
    desconto = salario * 0.08
elif salario <= 2919.72:
    desconto = salario * 0.09
elif salario <= 5839.45:
    desconto = salario * 0.11
else:
    desconto = 5839.45 * 0.11
print(("Desconto do INSS: R$ {:.2f}").format(desconto))