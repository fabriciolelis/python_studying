ano = int(input('Digite o ano a ser analizado: '))
if ano % 4 == 0:
    if ano % 100 == 0:
        if ano % 400 == 0:
            print('{} é um ano bissexto'.format(ano))
        else:
            print('{} não é um ano bissexto'.format(ano))
    else:
        print('{} é um ano bissexto'.format(ano))
else:
    print('{} não é um ano bissexto!'.format(ano))
