def menor_nome(lista):
    menor = lista[0].lower().strip()
    for element in lista:
        if menor > element.lower().strip():
            menor = element.lower().strip()
    return print(menor.capitalize())


lista = ["larissa", "joão", "fabricio", "    Ju", "Solange    ", "Julianne", "Ana", "alice"]

menor_nome(lista)
