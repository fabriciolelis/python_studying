from random import randint
from time import sleep

print('-=-' * 20)
print('Vou pensar em um número entre 0 e 10. Tente adivinhar...')
print('-=-' * 20)

n = randint(0, 5)
acertou = False
tentativas = 0

while not acertou:
    resposta = int(input('Em que número eu pensei? '))
    print('PROCESSANDO...')
    sleep(0.5)
    if n == resposta:
        acertou = True
    else:
        print('TENTE NOVAMENTE!')
    tentativas += 1

print('Você ACERTOU!! Foi no número {} que pensei. Você precisou de {} tentativas'.format(n, tentativas))
