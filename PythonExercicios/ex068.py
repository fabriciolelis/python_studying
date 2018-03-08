from random import randint

print('=-' * 20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-' * 20)

vitorias = 0

while True:
    venceu = False
    computador = randint(0, 10)
    jogador = int(input('Digite um valor: '))
    resposta = ' '
    soma = computador + jogador
    while resposta not in 'PpIi':
        resposta = input('Par ou ímpar? [P/I] ').strip().upper()[0]  # pega apenas o primeiro caracter da resposta
    if soma % 2 == 0:
        resultado = 'PAR'
    else:
        resultado = 'ÍMPAR'
    if (resultado == 'PAR' and resposta in 'Pp') or (resultado == 'ÍMPAR' and resposta in 'Ii'):
        venceu = True
        vitorias += 1
    print('-' * 20)
    print(f'Você jogou {jogador} e o computador {computador}. Total de {soma} DEU {resultado}')
    print('-' * 20)
    if venceu:
        print('Você VENCEU!'
              'Vamos jogar novamente...')
        print('=-' * 20)
    else:
        print('Você PERDEU!')
        break
print(f'GAME OVER! Você venceu {vitorias} vezes.')
