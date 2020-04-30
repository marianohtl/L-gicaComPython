p1 = float(input())
p2 = float(input())
p3 = float(input())
f = float(input())


def media_frequencia(p1,p2,p3,f):
  m = round((p1 * 2 + p2 * 2 + p3 * 3)/7,1)

  print("Frequencia: {:.0f}%".format(f * 100))
  print("Media: {:.1f}".format(m))
  if (f < 0.75):
    print("Aluno reprovado por faltas!")
  elif(m > 9.0):
    print("Aluno aprovado com louvor!")
  elif(m >= 6.0 and m <= 9.0):
    print("Aluno aprovado!")
  elif(m >= 4.0 and m < 6.0):
    print("Aluno de recuperação!")
  elif(m < 4):
    print("Aluno reprovado!")

media_frequencia(p1,p2,p3,f)