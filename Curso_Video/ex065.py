opcao = ' '
count = 0
soma = 0
maior = 0
menor = 0
while opcao not in 'Nn':
    num = int(input('Digite um número: '))
    if count == 0:
        maior = num
        menor = num
    if maior < num:
        maior = num
    if menor > num:
        menor = num
    soma += num
    count += 1
    opcao = input('Deseja continuar [S/N]? ')

media = soma / count
print('Você digitou {} números. A média dos valores digitados foi {}, '
      'o menor valor {} e o maior valor {}.'.format(count, media, menor, maior))
