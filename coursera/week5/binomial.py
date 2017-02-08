def fatorial(n):
    fatorial_value = 1
    while n > 1:
        fatorial_value = n * fatorial_value;
        n = n - 1
    return fatorial_value

n = int(input("Digite o valor de n: "))
k = int(input("Digite o valor de k: "))

binomio = fatorial(n) // ( fatorial(k) * fatorial(n - k) )
print("O valor do binomio é ", binomio)
