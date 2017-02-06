n = int(input("Digite o valor de inteiro: "))

fatorial = 1

if n == 0:
    print(1)
while n > 0:
    fatorial = n * fatorial
    n = n - 1
print(fatorial)
