nome = input('Digite seu nome completo: ')
separados = nome.split()
print('Seu primeiro nome {}'.format(separados[0]))
print('Seu último nome {}'.format(separados[len(separados) - 1]))
