fhand = open('words.txt')

dic = dict()
count = 1
for line in fhand:
    line = line.rstrip()
    if line in dic:
        continue
    dic[line] = count
    count = count + 1

print(dic)
