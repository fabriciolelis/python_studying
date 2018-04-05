soma_idades = 0
mais_velho = ''
idade_mais_velho = 0
menores_vinte = 0

for i in range(1, 5):
    print('---- {}ª PESSOA ----'.format(i))
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ')
    soma_idades += idade
    if sexo.upper() == 'M' and idade_mais_velho < idade:
        mais_velho = nome
        idade_mais_velho = idade
    if sexo.upper() == 'F' and idade < 20:
        menores_vinte += 1

media_idades = soma_idades / 4
print('A média de idade do grupo é de {:.1f} anos.'.format(media_idades))
print('O homem mais velho tem {} anos e se chama {}.'.format(idade_mais_velho, mais_velho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(menores_vinte))
