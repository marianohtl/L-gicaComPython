n = int(input())

def par_impar(n):
    modulo = n%2
    if(modulo == False):
        print("O numero eh {} e ele eh par".format(n))
    else:
      print("O numero eh {} e ele eh impar".format(n))

par_impar(n)