print('=-' * 20)
print('{:^30}'.format('LÉLIS BANK'))
print('=-' * 20)

valor = int(input('Digite o valor a ser sacado: R$'))
notas_50 = valor // 50
resto_50 = valor % 50
notas_20 = resto_50 // 20
resto_20 = resto_50 % 20
notas_10 = resto_20 // 10
resto_10 = resto_20 % 10
notas_1 = resto_10 // 1
print(f'Total de {notas_50} cédulas de R$50.00\n'
      f'Total de {notas_20} cédulas de R$20.00\n'
      f'Total de {notas_10} cédulas de R$10.00\n'
      f'Total de {notas_1} cédulas de R$1.00')
print('=' * 40)
print(f'Volte sempre ao LÉLIS BANK! Tenha um bom dia!')

