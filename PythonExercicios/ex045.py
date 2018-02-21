from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
print('Suas opções:\n'
      '[ 0 ] PEDRA\n'
      '[ 1 ] PAPEL\n'
      '[ 2 ] TESOURA')

jogador_opcao = int(input('Qual a sua jogada? '))
computador_opcao = randint(0, 2)

print('JO')
sleep(0.4)
print('KEN')
sleep(0.4)
print('PO!!!')
sleep(0.4)

print('-=-' * 10)
print('Computador jogou {}\n'
      'Jogador jogou {}'.format(itens[computador_opcao], itens[jogador_opcao]))
print('-=-' * 10)
if computador_opcao == jogador_opcao:
    print('EMPATE')
elif (jogador_opcao == 0 and computador_opcao == 2) or jogador_opcao > computador_opcao:
    print('Você Venceu!!!')
elif (computador_opcao == 0 and jogador_opcao == 2) or computador_opcao > jogador_opcao:
    print('Computador Venceu!!!')
