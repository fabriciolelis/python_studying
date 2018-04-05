peso = float(input('Peso da 1ª pessoa: '))
maior = peso
menor = peso
for i in range(2, 6):
    peso = float(input('Peso da {}ª pessoa: '.format(i)))
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
print('O maior peso lido foi de {:.2f}Kg\n'
      'O menor peso lido foi de {:.2f}Kg'.format(maior, menor))
