n = int(input('Digite um número: '))
print('Analisando o número {}'.format(n))
print('Unidade: {}'.format(n % 10))
print('Dezena: {}'.format(n % 100 // 10))
print('Centena: {}'.format(n % 1000 // 100))
print('Milhar: {}'.format(n // 1000))

u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
