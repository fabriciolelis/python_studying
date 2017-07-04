def busca(lista, elemento):
    primeiro = 0
    ultimo = len(lista) - 1

    while primeiro <= ultimo:
        metade = (primeiro + ultimo) // 2
        print(metade)
        if elemento == lista[metade]:
            return metade
        if elemento < lista[metade]:
            ultimo = metade - 1
        else:
            primeiro = metade + 1
    return False
