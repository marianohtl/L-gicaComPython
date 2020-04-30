# Coeficientes Binomial S2
def fatorial(x):
    i = 0
    f = 1
    while i < x:
        i = i + 1
        f = f * i
    return f

n = int(input('Digite o Numerador do Binomial: '))
p = int(input('Digite o Denominador do Biomial: '))
if n >= p:
    n_fatorial = fatorial(n)
    p_fatorial = fatorial(p)
    n_p = n - p
    sub_fatorial = fatorial(n_p)
    coefBi = n_fatorial / (p_fatorial * sub_fatorial)
    print(int(coefBi))
else:
    print('Não é possível fazer esse cálculo!')