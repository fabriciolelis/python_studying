n = 0
soma = 0
count = 0
while n != 999:
    n = int(input('Digite um número: '))
    if n != 999:
        soma += n
        count += 1
print('O total de números digitados foi {} e a soma entre eles foi de {}.'.format(count, soma))