from random import randint
from time import sleep

print('Suas opções:\n'
      '[ 0 ] PEDRA\n'
      '[ 1 ] PAPEL\n'
      '[ 2 ] TESOURA')
jogador_opcao = int(input('Qual a sua jogada? '))
jogador_escolha = ''
computador_escolha = ''

if jogador_opcao == 0:
    jogador_escolha = 'Pedra'
elif jogador_opcao == 1:
    jogador_escolha = 'Papel'
elif jogador_opcao == 2:
    jogador_escolha = 'Tesoura'

computador_opcao = randint(0, 2)
if computador_opcao == 0:
    computador_escolha = 'Pedra'
elif computador_opcao == 1:
    computador_escolha = 'Papel'
elif computador_opcao == 2:
    computador_escolha = 'Tesoura'

print('JO')
sleep(0.4)
print('KEN')
sleep(0.4)
print('PO!!!')
sleep(0.4)

print('-=-' * 10)
print('Computador jogou {}\n'
      'Jogador jogou {}'.format(computador_escolha, jogador_escolha))
print('-=-' * 10)
if computador_opcao == jogador_opcao:
    print('EMPATE')
elif (jogador_opcao == 0 and computador_opcao == 2) or jogador_opcao > computador_opcao:
    print('Você Venceu!!!')
elif (computador_opcao == 0 and jogador_opcao == 2) or computador_opcao > jogador_opcao:
    print('Computador Venceu!!!')
