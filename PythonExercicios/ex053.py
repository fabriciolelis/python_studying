frase = input('Digite a frase: ').replace(" ", "").strip()
invertido = frase.replace(" ", "")[::-1]
print('O inverso de {} é {}'.format(frase.upper(), invertido.upper()))
if invertido == frase:
    print('Temos um palíndromo!')
else:
    print('Não temos um palíndromo')
