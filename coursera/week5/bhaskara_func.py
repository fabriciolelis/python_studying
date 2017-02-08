import math

def delta (a, b, c):
    return b ** 2 - 4 * a * c

a = float(input("Digite o primeiro coeficiente: "))
b = float(input("Digite o segundo coeficiente: "))
c = float(input("Digite o terceiro coeficiente: "))

delta_valor = delta(a, b, c)

if delta_valor < 0:
	print("esta equação não possui raízes reais")
elif delta_valor == 0:
	raiz = -b / (2 * a)
	print("a raiz desta equação é", raiz)
else:
	raiz1 = (-b - math.sqrt(delta)) / (2 * a)
	raiz2 = (-b + math.sqrt(delta)) / (2 * a)
	print("as raízes da equação são", raiz1,"e", raiz2)
