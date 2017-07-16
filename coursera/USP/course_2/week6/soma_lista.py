def soma_lista(lista):
    tamanho_lista = len(lista)
    if tamanho_lista == 1:
        return lista[0]
    else:
        return lista[tamanho_lista-1] + soma_lista(lista[0:tamanho_lista-1])