from random import randint
from time import sleep

print('Suas opções:\n'
      '[ 0 ] PEDRA\n'
      '[ 1 ] PAPEL\n'
      '[ 2 ] TESOURA')
opcao = int(input('Qual a sua jogada? '))
sua_escolha = ''
comp_escolha = ''

if opcao == 0:
    sua_escolha = 'Pedra'
elif opcao == 1:
    sua_escolha = 'Papel'
elif opcao == 2:
    sua_escolha = 'Tesoura'

comp_opcao = randint(0, 2)
print('Computador opção', comp_opcao)
if comp_opcao == 0:
    comp_escolha = 'Pedra'
elif comp_opcao == 1:
    comp_escolha = 'Papel'
elif comp_opcao == 2:
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
