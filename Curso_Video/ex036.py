valor_casa = float(input('Valor da Casa: R$ '))
salario = float(input('Salário do comprador: R$ '))
anos = int(input('Quantos anos de financiamento? '))
porcentagem_maxima = salario * 30 / 100
parcelas = valor_casa / (anos * 12)
print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}'.format(valor_casa, anos, parcelas))
if parcelas < porcentagem_maxima:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')
