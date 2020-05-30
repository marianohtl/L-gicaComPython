strings=""
letras=""
def contando_caracteres(strings,letra):
  i=0
  for carac in strings:
    if carac == letra:
      i = i +1
  if i == 0:
    print("Caractere nao encontrado.")
  else:
    print(f"O caractere buscado ocorre {i} vezes na sequencia.")


strings = input()
letra = input()
contando_caracteres(strings,letra)
