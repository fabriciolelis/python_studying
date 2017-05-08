def chop(lista):
    del lista[0]
    del lista[len(lista) - 1]
    return None


t = ['a', 'b', 'c', 'd']
chop(t)
print(t)
