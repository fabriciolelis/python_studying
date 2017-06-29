from random import randint

class Lista_grande:

    def lista_grande(self, n):
        lista = []
        for i in range(n):
            numero = randint(0, 1000)
            lista.append(numero)
        return lista

l = Lista_grande()
print(l.lista_grande(100))
