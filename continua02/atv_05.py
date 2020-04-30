salario = float(input())

def inss(salario):
  if(salario <= 1751.81):
     desc =  salario * 0.08
  elif(salario >= 1751.82 and salario <= 2919.72):
     desc =  salario * 0.09    
  elif(salario >= 2919.73 and salario <= 5839.45):
     desc =  salario * 0.11    
  else:
    desc = 5839.45 * 0.11 
    
  print("Desconto do INSS: R$ {:.2f}".format(desc))

inss(salario)