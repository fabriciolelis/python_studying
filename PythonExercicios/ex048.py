soma = 0
count = 0
for i in range(1, 500):
    if i % 3 == 0 and i % 2 != 0:
        soma += i
        count += 1
print('A quantidade de valores somados {} e a soma total {}'.format(count, soma))
