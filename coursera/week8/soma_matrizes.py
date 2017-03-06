def soma_matrizes(m1, m2):
    matriz_soma = []
    quant_linhas_m1 = len(m1)
    quant_colunas_m1 = len(m1[0])
    quant_linhas_m2 = len(m2)
    quant_colunas_m2 = len(m2[0])
    if (quant_linhas_m1 != quant_linhas_m2):
        return False
    if (quant_colunas_m1 != quant_colunas_m2):
        return False
    for i in range(quant_linhas_m1):
        matriz_soma.append([])
        for j in range(quant_colunas_m1):
            soma = m1[i][j] + m2[i][j]
            matriz_soma[i].append(soma)
    return matriz_soma


m1 = [[1], [2], [3]]
m2 = [[2, 3, 4], [5, 6, 7]]
print(soma_matrizes(m1, m2))
