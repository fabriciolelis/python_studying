inteiro = int(input("Digite o valor de inteiro: "))
soma = 0

while (inteiro // 10) != 0:
    soma += inteiro % 10
    inteiro = inteiro // 10
soma += inteiro
print(soma)
