def ordena(lista):
    fim = len(lista)
    for i in range(fim - 1):
        posicao_do_minimo = i
        for j in range(i + 1, fim):
            if lista[j] < lista[posicao_do_minimo]:
                posicao_do_minimo = j
        lista[i], lista[posicao_do_minimo] = lista[posicao_do_minimo], lista[i]
    return lista

lista_teste = [554, 700, 646, 132, 681, 267, 3, 607, 579, 473, 242, 200, 49, 780, 782, 212, 132, 139, 857, 601, 619, 705, 624, 298, 999, 617, 845, 575, 670, 233, 99, 652, 354, 371, 526, 37, 829, 743, 509, 90]

print(ordena(lista_teste))