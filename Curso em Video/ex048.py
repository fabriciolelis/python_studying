soma = 0
count = 0
for i in range(1, 501, 2):  # mesma sacada para imprimir os pares da questão anterior
    if i % 3 == 0:
        soma += i
        count += 1
print('A quantidade de valores somados {} e a soma total {}'.format(count, soma))
