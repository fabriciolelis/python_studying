from random import choice

primeiro = input('Primeiro aluno: ')
segundo = input('Segundo aluno: ')
terceiro = input('Terceiro aluno: ')
quarto = input('Quarto aluno: ')
print('O aluno escolhido foi {}'.format(choice([primeiro, segundo, terceiro, quarto])))
