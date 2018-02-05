from random import shuffle
primeiro = input('Digite o nome de um Aluno: ')
segundo = input('Digite o nome de um Aluno: ')
terceiro = input('Digite o nome de um Aluno: ')
quarto = input('Digite o nome de um Aluno: ')
lista = [primeiro, segundo, terceiro, quarto]
shuffle(lista)
print('A sequência de apresentação será {}'.format(lista))
