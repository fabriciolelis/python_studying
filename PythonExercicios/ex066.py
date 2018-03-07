count = 0
soma = 0
while True:
    num = int(input('Digite um valor inteiro (999 para parar): '))
    if num == 999:
        break
    soma += num
    count += 1
print(f'A quantidade número digitados {count} e a soma entre eles foi de {soma}.')