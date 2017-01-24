import math

P1X = int(input("Digite a coordenada X do primeiro ponto: "))
P1Y = int(input("Digite a coordenada Y do primeiro ponto: "))
P2X = int(input("Digite a coordenada X do segundo ponto: "))
P2Y = int(input("Digite a coordenada Y do segundo ponto: "))

diferença1 = ( P2X - P1X ) ** 2
diferença2 = ( P2Y - P1Y ) ** 2

distancia = math.sqrt(diferença1 + diferença2)

if distancia >= 10:
	print("longe")
else:
	print("perto") 
