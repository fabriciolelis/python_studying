import math
def soma_hipotenusas(n):
	soma_hipotenusa = 0
	hipotenusa = 1
	while hipotenusa <= n:
		if éHipotenusa(hipotenusa):
			soma_hipotenusa = soma_hipotenusa + hipotenusa
			hipotenusa = hipotenusa + 1
		else:
			hipotenusa = hipotenusa +1
	return soma_hipotenusa

def éHipotenusa(x):
	cateto1 = 1
	cateto2 = 1
	while cateto1 < x:
		while cateto2 < x:
			quadradocateto1 = cateto1 ** 2
			quadradocateto2 = cateto2 ** 2
			quadradohipotenusa = quadradocateto1 + quadradocateto2
			hipotenusa = math.sqrt(quadradohipotenusa)
			if hipotenusa == x:
				return True
			else:
				cateto2 = cateto2 + 1
		cateto1 = cateto1 + 1
		cateto2 = 1
	return False
print(soma_hipotenusas(15))
