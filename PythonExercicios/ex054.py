from datetime import date

maiores = 0
menores = 0

for i in range(1, 8):
    ano = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(i)))
    if date.today().year - ano >= 18:
        maiores += 1
    else:
        menores += 1
print('Ao todo tivemos {} pessoas maiores de idade\n'
      'E também tivemos {} pessoas menores de idade'.format(maiores, menores))
