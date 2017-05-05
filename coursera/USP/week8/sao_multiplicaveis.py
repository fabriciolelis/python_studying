def sao_multiplicaveis(m1, m2):
    quant_colunas_m1 = len(m1[0])
    quant_linhas_m2 = len(m2)
    if(quant_colunas_m1 != quant_linhas_m2):
        return False
    else:
        return True

m1 = [[1], [2], [3]]
m2 = [[1, 2, 3]]
print(sao_multiplicaveis(m1, m2))
