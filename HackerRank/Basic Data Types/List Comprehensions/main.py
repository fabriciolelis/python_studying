if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    print([ [i, j, m] for i in range(x+1) for j in range(y+1) for m in range(z+1) if (( i + j + m) != n )])