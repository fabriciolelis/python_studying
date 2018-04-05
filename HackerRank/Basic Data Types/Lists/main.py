if __name__ == '__main__':
    N = int(input())
    lista = []
    for i in range(0, N):
        entrada = input().split()    
        if 'insert' in entrada:
            lista.insert(int(entrada[1]), int(entrada[2]))
        elif 'remove' in entrada:
            lista.remove(int(entrada[1]))
        elif 'append' in entrada:
            lista.append(int(entrada[1]))
        elif 'sort' in entrada:
            lista.sort()
        elif 'pop' in entrada:
            lista.pop()
        elif 'reverse' in entrada:
            lista = lista[::-1]
        elif 'print' in entrada:
            print(lista)
    lista.clear()