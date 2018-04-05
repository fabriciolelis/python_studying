print('=' * 40)
print('{:^40}'.format('10 Termos de uma PA'))
print('=' * 40)
primeiro_termo = int(input('Primeiro termo da PA: '))
razao = int(input('Razão: '))
decimo = primeiro_termo + (10 - 1) * razao
for i in range(primeiro_termo, decimo + razao, razao):
    print(i, end=" ")
