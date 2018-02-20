from random import randint
from time import sleep

print('Suas opções:\n'
      '[ 1 ] PEDRA\n'
      '[ 2 ] PAPEL\n'
      '[ 3 ] TESOURA')
opcao = int(input('Qual a sua jogada? '))
sua_escolha = ''
if opcao == 1:
    sua_escolha = 'Pedra'
elif opcao == 2:
    sua_escolha == 'Papel'
elif opcao == 3:
    sua_escolha = 'Tesoura'
comp_opcao = randint(1, 3)
comp_escolha = ''
print('Computador opção', comp_opcao)
if comp_opcao == 1:
    comp_escolha = 'Pedra'
elif comp_opcao == 2:
    comp_escolha = 'Papel'
elif opcao == 3:
    comp_escolha = 'Tesoura'
print('JO')
sleep(0.4)
print('KEN')
sleep(0.4)
print('PO!!!')
sleep(0.4)
print('-=-' * 10)
print('Computador jogou {}\n'
      'Jogador jogou {}'.format(comp_escolha, sua_escolha))
print('-=-' * 10)