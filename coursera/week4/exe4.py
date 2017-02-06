inteiro = int(input("Digite o valor de inteiro: "))

atual = inteiro % 10
anterior = inteiro
adjacente = False

while (inteiro // 10) != 0 and not adjacente:
    if (atual == anterior):
        adjacente = True
    anterior = atual
    atual = (inteiro // 10) % 10
    inteiro = inteiro // 10

if adjacente:
    print("sim")
else:
    print("não")
