while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n < 0:
        break
    print('--' * 6)
    for i in range(11):
        print(f'{n} x {i} = {n*i}')
    print('--' * 6)
print('PROGRAMA TABUADA ENCERRADO. Volte Sempre!')
