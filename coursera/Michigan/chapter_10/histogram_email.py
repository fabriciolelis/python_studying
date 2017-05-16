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
    count[words[1]] = count.get(words[1], 0) + 1

emails = list()
for k, v in count.items():
    emails.append((v, k))
emails.sort(reverse=True)

for k, v in emails[0:1]:
    print(v, k)
