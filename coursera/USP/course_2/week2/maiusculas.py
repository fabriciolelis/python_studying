def maiusculas(frase):
    letras_maiusculas = ''
    for c in frase:
        if 65 <= ord(c) <= 90:
            letras_maiusculas = letras_maiusculas + c

    return letras_maiusculas

frase = 'Programamos em python 2?'

maiusculas(frase)
