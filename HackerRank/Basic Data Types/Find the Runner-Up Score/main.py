if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    lista = list(arr)
    lista.sort()
    max = max(lista)
    while max in lista:
        lista.remove(max)
    print(lista[len(lista)-1])