largura = int(input("Digite a largura: "))
altura = int(input("Digite a altura: "))
i = 0
while i < altura:
    j = 0
    while j < largura:
        print("#", end="")
        j += 1
    print()
    i += 1
