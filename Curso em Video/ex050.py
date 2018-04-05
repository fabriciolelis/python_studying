soma = 0
for i in range(1, 7):
    digitado = int(input('Digite o {}º número: '.format(i)))
    if digitado % 2 == 0:
        soma += digitado
print('A soma de todos os números pares digitados por você foi {}.'.format(soma))
