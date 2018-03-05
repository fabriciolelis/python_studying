print('=' * 40)
print('{:^40}'.format('10 Termos de uma PA'))
print('=' * 40)

primeiro_termo = int(input('Primeiro termo da PA: '))
razao = int(input('Razão: '))
n = 1
termos = 1
total = 10

while termos != 0:
    while n <= total:
        print(primeiro_termo + (n-1) * razao, end=' → ')
        n += 1
    print('PAUSA')
    termos = int(input('Quantos termos você quer mostrar mais? '))
    total += termos
print('Progressão finalizada com {} termos mostrados.'.format(total))
