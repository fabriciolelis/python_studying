from random import randint


def lista_grande(n):
    lista = []
    for i in range(n):
        numero = randint(0, 1000)
        lista.append(numero)
    return lista

print(lista_grande(100))
