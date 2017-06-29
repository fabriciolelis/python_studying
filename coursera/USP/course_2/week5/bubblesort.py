def bubble_sort(lista):
    fim = len(lista)

    for i in range(fim -1, 0, -1):
        for j in range(i):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
        if i > 1:
            print(lista)
    return lista

bubble_sort([5, 1, 4, 2, 8])