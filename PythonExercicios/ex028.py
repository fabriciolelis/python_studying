from random import randint
from time import sleep

print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)

n = randint(0, 5)
resposta = int(input('Em que número eu pensei? '))

print('PROCESSANDO...')
sleep(0.9)

if n == resposta:
    print('PERDI! Foi no número {} que pensei.'.format(n))
else:
    print('GANHEI! Eu pensei no número {} e não no {}.'.format(n, resposta))
