maior18 = 0
homens = 0
mulheres_menor20 = 0

while True:
    print('-' * 20)
    print('CADASTRE UMA PESSOA')
    print('-' * 20)
    idade = int(input('Idade: '))
    if idade > 18:
        maior18 += 1
    sexo = ' '
    while sexo not in 'MF':
        sexo = input('Sexo: [M/F] ').strip().upper()[0]
    if sexo == 'M':
        homens += 1
    elif sexo.upper() == 'F' and idade < 20:
        mulheres_menor20 += 1
    resposta = ' '
    print('-' * 20)
    while resposta not in 'SN':
        resposta = input('Quer continuar? [S/N]').strip().upper()[0]
    if resposta == 'N':
        break
print('==== FIM DO PROGRAMA ====')
print(f'Total de pessoas com mais de 18 anos: {maior18}\n'
      f'Ao todo temos {homens} cadastrados\n'
      f'E temos {mulheres_menor20} mulheres com menos de 20 anos.')