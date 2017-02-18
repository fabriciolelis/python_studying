largura = int(input("Digite a largura: "))
altura = int(input("Digite a altura: "))
i = 0
while i < altura:
    j = 0
    while j < largura:
        if(i == 0 or i == (altura - 1)):
            print("#", end="")
        elif (j == 0 or j == (largura - 1)):
            print("#", end="")
        else:
            print(" ", end="")
        j = j + 1
    print()
    i = i + 1
