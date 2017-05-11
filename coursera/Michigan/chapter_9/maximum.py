fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

dic = dict()
bigEmail = None
bigValue = None
for line in fhand:
    words = line.split()
    if len(words) == 0:
        continue
    if words[0] != 'From':
        continue
    dic[words[1]] = dic.get(words[1], 0) + 1
for key, value in dic.items():
    if bigValue is None or value > bigValue:
        bigValue = value
        bigEmail = key
print(bigEmail, bigValue)
