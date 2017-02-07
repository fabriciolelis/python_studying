n = int(input("Digite o valor de inteiro: "))

fatorial = 1

while n > 1:
    fatorial = n * fatorial
    n = n - 1
print(fatorial)
