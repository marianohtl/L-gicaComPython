Atividade contínua 4 da matéria de lógica de progrmação.

AC4 - Praticando Lógica de Programação

Faça um código em Python que:

a) Peça para o usuário digitar a quantidade de nomes que irá digitar e armazene na variável n.
 Essa variável n deverá ser maior que 3 e menor que 10 (Validação de dados de entrada).
  O armazenamento da variável n deverá ser feito em uma lista "l".

b) Faça as seguintes implementações, nessa ordem:

1º) Adiciona o nome "Teste" no índice 3. (estava escrito "posição").

2º) Exclua o elemento de índice 2.

3º) Verifique quantas vezes você digitou o nome 'Ana'. Se for maior que 0,
 mostre o índice da primeira ocorrência.
Se for 0, mostre uma frase informando que o nome Ana não existe na lista.

4º) No final, mostre a lista ordenada.

OBS: Carregue seu arquivo em Python em anexo a esta AC.
"""

n = int(input("Quantos nomes você vai digitar?\n"))

while n <= 3 or n >= 10:
    print("Quantidade de nomes digitados inválida, digite um número maior que 3 ou menor que 10.")
    n = int(input("Quantos nomes você vai digitar?\n"))


# while True:
#     n = int(input("Quantos nomes você vai digitar?\n"))
#     if n > 3 and n < 10:
#         break
#     print("Quantidade de nomes digitados inválida, digite um número maior que 3 ou menor que 10.")

l = []
for i in range(n):
    nome = input("Digite o nome desejado:\n")
    l.append(nome)

# l = []
# i = 0
# while i < n:
#     nome = input("Digite o nome desejado:\n")
#     l.append(nome)
#     i += 1
#
#
# l = [None] * n
# i = 0
# while i < n:
#     nome = input("Digite o nome desejado:\n")
#     l[i] = nome
#     i += 1
#
# for i in range(n):
#     nome = input("Digite o nome desejado:\n")
#     l[i] = nome

l.insert(3, 'Teste')
l.pop(2)
# del l[2]

anas = 0
for nome in l:
    if nome == 'Ana':
        anas += 1

if anas > 0:
    # for i in range(n):
    #     if l[i] == 'Ana':
    #         print(i)
    #         break
    i = 0
    while l[i] != 'Ana':
        i += 1
    print(f"Ana aparece no índice {i}")
else:
    print('Ana não está na lista')

# indice = n
# anas = 0
# for i in range(n):
#     if l[i] == 'Ana':
#         anas += 1
#         indice = min(i, indice)
# if anas = 0:
#     print(indice)
# else:
#     print('Ana não está na lista')

# anas = l.count('Ana')
# if anas > 0:
#     print(l.index('Ana'))
# else:
#     print('Ana não está na lista')

l = sorted(l)
print(l)
# l.sort()