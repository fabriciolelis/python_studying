import random
primeiro = input('Digite o nome de um Aluno: ')
segundo = input('Digite o nome de um Aluno: ')
terceiro = input('Digite o nome de um Aluno: ')
quarto = input('Digite o nome de um Aluno: ')
print('A sequência de apresentação será {}'.format(random.sample([primeiro, segundo, terceiro, quarto], 4)))
