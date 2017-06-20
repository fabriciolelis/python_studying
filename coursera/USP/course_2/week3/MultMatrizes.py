import sao_multiplicaveis


def mult_matrizes(A, B):
    if sao_multiplicaveis.sao_multiplicaveis(A, B):
        num_linhas_A, num_colunas_A = len(A), len(A[0])
        num_linhas_B, num_colunas_B = len(B), len(B[0])

        C = []
        for linha in range(num_linhas_A):
            # começando nova linha
            C.append([])
            for coluna in range(num_colunas_B):
                # adicionando nova coluna na linha
                C[linha].append(0)
                for k in range(num_colunas_A):
                    C[linha][coluna] += A[linha][k] * B[k][coluna]
        return C
    else:
        return "Essas matrizes não são multiplicavéis"


A = [[1, 2, 3], [4, 5, 6]]
B = [[1, 2], [3, 4], [5, 6]]
print(mult_matrizes(A, B))
