print('{:=^40}'.format(' LOJAS FABRICIO '))  # ^ - CENTRALIZADO
preco = float(input('Preço das compras: R$'))

print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')

opcao = int(input('Qual é a sua opção? '))

if opcao == 1:
    desconto = preco * 10 / 100
    valor = preco - desconto
elif opcao == 2:
    desconto = preco * 5 / 100
    valor = preco - desconto
elif opcao == 3:
    parcelas = preco / 2
    valor = preco
    print('Sua compra será parcela em 2x de R${:.2f} SEM JUROS'.format(parcelas))
elif opcao == 4:
    qunt_parcelas = int(input('Quantas parcelas? '))
    juros = preco * 20 / 100
    valor = preco + juros
    parcelas = valor / qunt_parcelas
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS.'.format(qunt_parcelas, parcelas))
else:
    valor = preco
    print('Está opção não existe. Digite uma opção válida!')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, valor))
