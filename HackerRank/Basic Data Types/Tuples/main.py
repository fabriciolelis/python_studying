if __name__ == '__main__':
    n = int(input())
    integer_list = list(map(int, input().split()))
    t = ()
    for i in range(len(integer_list)):
        temp = (integer_list[i], )
        t += temp
    print(hash(t))