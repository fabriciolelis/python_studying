def maximo(x, y, z):
    if x > y and x > z:
        return x
    elif y > z:
        return y
    else:
        return z

print(maximo(12, 20, 30))
