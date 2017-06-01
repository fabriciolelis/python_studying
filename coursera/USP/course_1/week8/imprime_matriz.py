def imprime_matriz(matriz):
    linhas = len(matriz)
    colunas = len(matriz[0])
    for i in range(linhas):
        for j in range(colunas):
            if j < colunas - 1:
                print (matriz[i][j],  end=' ')
            else:
                print(matriz[i][j], end='')
        print()

a = [[1, 2, 3], [4, 5, 6]]
imprime_matriz(a)
