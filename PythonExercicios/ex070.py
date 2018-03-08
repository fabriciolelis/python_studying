total_gasto = 0
maior_1000 = 0
mais_barato = ''
mais_barato_valor = 0

while True:
    nome = input('Nome do produto: ')
    preco = float(input('Preço: R$ '))
    if total_gasto == 0 or preco < mais_barato_valor:
        mais_barato = nome
        mais_barato_valor = preco
    total_gasto += preco
    if preco > 1000:
        maior_1000 += 1
    respota = ' '
    while respota not in 'SN':
        respota = input('Deseja continuar? [S/N] ').strip().upper()[0]
    if respota in 'N':
        break
print('==== FIM DO PROGRAMA ====')
print(f'O total da compra foi R${total_gasto:.2f}\n'
      f'Temos {maior_1000} produtos mais de R$1000.00\n'
      f'O produto mais barato foi {mais_barato} que custa R${mais_barato_valor:.2f}')
