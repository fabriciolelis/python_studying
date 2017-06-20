class Triangulo:

    def __init__(self, lado1, lado2, lado3):
        self.a = lado1
        self.b = lado2
        self.c = lado3

    def perimetro(self):
        return self.a + self.b + self.c

    def retangulo(self):
        hipotenusa = self.c ** 2
        cateto1 = self.a ** 2
        cateto2 = self.b ** 2
        soma_catetos = cateto1 + cateto2
        if hipotenusa == soma_catetos:
            return True
        else:
            return False

    def semelhantes(self, triangulo):
        lista1 = [self.a, triangulo.a]
        lista2 = [self.b, triangulo.b]
        lista3 = [self.c, triangulo.c]
        lista1.sort()
        lista2.sort()
        lista3.sort()
        if lista1[1] % lista1[0] != 0:
            return False
        elif lista2[1] % lista2[0] != 0:
            return False
        elif lista3[1] % lista3[0] != 0:
            return False
        else:
            return True

def main():
    t = Triangulo(3, 4, 5)
    t1 = Triangulo(2, 2, 2)
    t2 = Triangulo(4, 4, 4)
    print(t.a)
    print(t.b)
    print(t.c)
    print(t.perimetro())
    print(t.retangulo())
    print(t1.semelhantes(t2))


main()