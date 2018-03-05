num = int(input('Digite um número para calcular o Fatorial: '))

fatorial = 1
count = num
while count > 1:
    fatorial *= count
    count -= 1
print('O fatorial de {} é {}'.format(num, fatorial))
