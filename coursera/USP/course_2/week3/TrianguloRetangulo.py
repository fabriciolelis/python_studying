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

def main():
    t = Triangulo(3, 4, 5)
    print(t.a)
    print(t.b)
    print(t.c)
    print(t.perimetro())
    print(t.retangulo())


main()