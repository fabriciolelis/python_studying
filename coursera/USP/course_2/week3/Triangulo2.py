class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.a = lado1
        self.b = lado2
        self.c = lado3

    def perimetro(self):
        return self.a + self.b + self.c

    def tipo_lado(self):
        if (self.a == self.b) and (self.a == self.c):
            return 'equilátero'
        elif (self.a != self.b) and (self.a != self.c) and (self.b != self.c):
            return 'escaleno'
        else:
            return 'isóceles'


def main():
    t = Triangulo(3, 4, 4)
    print(t.a)
    print(t.b)
    print(t.c)
    print(t.perimetro())
    print(t.tipo_lado())


main()
