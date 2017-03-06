def imprime_matriz(matriz):
    for linha in range(len(matriz)):
        for coluna in range(len(matriz[0])):
            print (matriz[linha][coluna],  end = " ")
        print()


a = [[1, 2, 3], [4, 5, 6]]
imprime_matriz(a)
