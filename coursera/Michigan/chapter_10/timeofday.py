fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

count = dict()

for line in fhand:
    words = line.split()
    if len(words) == 0:
        continue
    if words[0] != 'From':
        continue
    hours = words[5].split(':')
    count[hours[0]] = count.get(hours[0], 0) + 1

lst = list()
for k, v in count.items():
    lst.append((k, v))

lst.sort()

for k, v in lst:
    print(k, v)
