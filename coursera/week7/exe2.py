def soma_elementos(lista):
    soma = 0;
    for value in lista:
        soma = soma + value
    return soma


lista1 = [2,3,4,5]
print(soma_elementos(lista1))
