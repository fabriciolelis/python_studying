def encontra_impares(lista):
    tamanho_lista = len(lista)
    if tamanho_lista == 1 and lista[0] % 2 != 0:
        nlista = [lista[0]]
        return nlista
    elif tamanho_lista == 1 and lista[0] % 2 == 0:
        return []
    elif lista[len(lista) - 1] % 2 != 0:
        alista = [lista[len(lista) - 1]]
        alista.extend(encontra_impares(lista[0:len(lista) - 1]))
        return alista
    else:
        alista = []
        alista.extend(encontra_impares(lista[0:len(lista) - 1]))
        return alista
