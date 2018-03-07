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
    while sexo not in 'MFmf':
        sexo = input('Sexo: [M/F] ')
    if sexo.upper() == 'M':
        homens += 1
    elif sexo.upper() == 'F' and idade < 20:
        mulheres_menor20 += 1
    resposta = ' '
    print('-' * 20)
    while resposta not in 'SNsn':
        resposta = input('Quer continuar? [S/N]')
    if resposta.upper() == 'N':
        break
print('==== FIM DO PROGRAMA ====')
print(f'Total de pessoas com mais de 18 anos: {maior18}\n'
      f'Ao todo temos {homens} cadastrados\n'
      f'E temos {mulheres_menor20} mulheres com menos de 20 anos.')