def ordenada(lista):
    atual = lista[0]
    for i in range(len(lista)):
        if atual > lista[i]:
            return False
        atual = lista[i]
    return True
