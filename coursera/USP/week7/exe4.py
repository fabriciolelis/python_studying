def remove_repetidos(lista):
    lista2 = []
    for value in lista:
        if value not in lista2:
            lista2.append(value)
    lista2.sort()
    return lista2

lista3 = [100,5,5,5,5,7,7,77,7,400,7,10,90, 400, 1000]
print(remove_repetidos(lista3))
