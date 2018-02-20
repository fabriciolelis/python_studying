from datetime import date

ano_nasc = int(input('Ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano_nasc
print('Quem nasceu em {} tem {} idade em {}.'.format(ano_nasc, idade, ano_atual))
if idade < 18:
    temp_alistamento = 18 - idade
    print('Ainda faltam {} anos para o alistamento.\n'
          'Seu alistamento será em {}'.format(temp_alistamento, ano_atual + temp_alistamento))
elif idade > 18:
    tempo_alistamento = ano_atual - (ano_nasc + 18)
    print('Você já deveria ter se alistado há {} anos.\n'
          'Seu alistamento foi em {}'.format(tempo_alistamento, ano_nasc + 18))
else:
    print('Você tem que se alistar IMEDIATAMENTE!')
