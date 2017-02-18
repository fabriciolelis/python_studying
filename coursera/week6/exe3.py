def éPrimo(y):
    fator = 2
    if y == 2:
        return True
    while y % fator != 0 and fator <= y/2:
        fator = fator + 1
    if y % fator == 0:
        return False
    else:
        return True

def n_primos(x):
    n = 2
    num_primos = 0
    while n <= x:
        if éPrimo(n):
            num_primos = num_primos + 1
        n = n + 1
    return num_primos

print(n_primos(6))
