def primeiro_lex(lista):
    primeiro = lista[0].strip()
    for elemento in lista:
        if primeiro > elemento:
            primeiro = elemento
    return primeiro

lista = (['AAAAAA', 'b'])

print(primeiro_lex(lista))
