print('=' * 40)
print('{:^40}'.format('10 Termos de uma PA'))
print('=' * 40)
primeiro_termo = int(input('Primeiro termo da PA: '))
razao = int(input('Razão: '))
for i in range(primeiro_termo, (razao * 10), razao):
    print(i)