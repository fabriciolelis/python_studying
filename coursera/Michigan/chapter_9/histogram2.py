fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

dic = dict()
for line in fhand:
    words = line.split()
    if len(words) == 0:
        continue
    if words[0] != 'From':
        continue
    domain = words[1].split('@')
    dic[domain[1]] = dic.get(domain[1], 0) + 1
print(dic)
