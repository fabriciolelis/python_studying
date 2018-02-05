import math

angulo = float(input('Digite o ângulo que você deseja: '))
x = math.radians(angulo)
print('O valor do cosseno do ângulo {} é {:.2f}'.format(angulo, math.cos(x)))
print('O valor do seno do ângulo {} é {:.2f}'.format(angulo, math.sin(x)))
print('O valor da tagente do ângulo {} é {:.2f}'.format(angulo, math.tan(x)))
