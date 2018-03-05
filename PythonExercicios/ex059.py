num1 = int(input('Primeiro Valor: '))
num2 = int(input('Segundo Valor: '))
opcao = 0
while opcao != 5:
    print('[ 1 ] somar\n'
          '[ 2 ] multiplicar\n'
          '[ 3 ] maior\n'
          '[ 4 ] novos números\n'
          '[ 5 ] sair do programa')
    opcao = int(input('Qual sua opção? '))
    if opcao == 1:
        print('A soma entre {} e {} é {}\n'.format(num1, num2, num1 + num2))
    elif opcao == 2:
        print('O produto entre {} e {} é {}\n'.format(num1, num2, num1 * num2))
    elif opcao == 3:
        if num1 > num2:
            maior = num1
        else:
            maior = num2
        print('O maior número entre {} e {} é {}\n'.format(num1, num2, maior))
    elif opcao == 4:
        num1 = int(input('Primeiro Valor: '))
        num2 = int(input('Segundo Valor: '))
print('Obrigado por usar o programa!')
