n = int(input("Digite um inteiro diferente de zero: "))
lista = []

while n != 0:
    lista.append(n)
    n = int(input("Digite um inteiro diferente de zero: "))

tamanho = len(lista) - 1
lista_inv = []
while tamanho >= 0:
    print(lista[tamanho])
    #lista_inv.append(lista[tamanho])
    tamanho = tamanho - 1
#print(lista_inv)
