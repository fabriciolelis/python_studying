fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

count = 0
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From: '):
        continue
    words = line.split()
    count = count + 1
    print(words[1])

print('There were', count, 'lines in the file with From as the first word')