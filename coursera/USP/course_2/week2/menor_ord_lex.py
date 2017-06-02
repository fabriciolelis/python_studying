def ordem_lex(lista):
    menor = lista[0].lower().strip()
    for element in lista:
        if menor > element.lower().strip():
            menor = element.lower().strip()
    return menor.capitalize()


lista = ["larissa", "joão", "fabricio", "    Ju", "Solange    ", "Julianne", "Ana", "alice"]

print(ordem_lex(lista))
