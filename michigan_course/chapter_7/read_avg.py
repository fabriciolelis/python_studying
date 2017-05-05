fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

count = 0
total = 0
for line in fhand:
    line = line.rstrip()
    if line.startswith('X-DSPAM-Confidence:'):
        count = count + 1
        pos = line.find(':')
        value = float(line[pos+2:])
        total = total + value

avg = total / count
print('Average spam confidence:', avg)