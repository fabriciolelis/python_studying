dias = int(input('Quantos dias alugados? '))
quilometros = float(input('Quantos quilômetros pecorridos? '))
total = dias * 60 + quilometros * 0.15
print('O total do aluguel por {} dias e {} Km pecorridos é R$ {}.'.format(dias, quilometros, total))
