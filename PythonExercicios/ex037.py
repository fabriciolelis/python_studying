num = int(input('Digite um número inteiro: '))
print('Escolha uma base para conversão:\n'
      '[ 1 ] converter para BINÁRIO\n'
      '[ 2 ] converter para OCTAL\n'
      '[ 3 ] converter para HEXADECIMAL')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print('{} convertido para BINÁRIO é igual a {:b}'.format(num, num))
elif opcao == 2:
    print('{} convertido para OCTAL é igual a {:o}'.format(num, num))
elif opcao == 3:
    print('{} convertido para HEXADECIMAL é igual a {:h}'.format(num, num))
else:
    print('Opção não existente')
