print('-' * 40)
print('{:^40}'.format('Sequência de Fibonacci'))
print('-' * 40)

termos = int(input('Quantos termos você quer mostrar? '))
fibo = 1
n = 1
anterior = 0
while n < termos:
    if n == 1:
        print(0, end=' → ')
    print(fibo, end=' → ')
    temp = fibo
    fibo = fibo + anterior
    anterior = temp
    n += 1
print('FIM')
