def dimensoes(matriz):
    linha = 0
    col_final = 0
    for linha in range(len(matriz)):
        coluna = 0
        for coluna in range(len(matriz[0])):
            coluna = coluna + 1
        linha = linha + 1
        col_final = coluna
    return str(linha) + "X" + str(col_final)

minha_matriz = [[1, 2], [3, 4]]
print(dimensoes(minha_matriz))
