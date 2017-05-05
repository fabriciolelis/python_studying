import math

def delta (a, b, c):
    return b ** 2 - 4 * a * c

def imprime_raizes(a, b, c):
    d = delta(a, b, c)
    if d < 0:
        print("essa equação não possui raízes reais")
    elif d == 0:
        raiz = -b / (2 * a)
        print("a raiz desta equação é", raiz)
    else:
        raiz1 = (-b - math.sqrt(d)) / (2 * a)
        raiz2 = (-b + math.sqrt(d)) / (2 * a)
        print("as raízes da equação são", raiz1, "e", raiz2)


a = float(input("Digite o primeiro coeficiente: "))
b = float(input("Digite o segundo coeficiente: "))
c = float(input("Digite o terceiro coeficiente: "))
imprime_raizes(a, b, c)
