fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

letters = list()
dic = dict()
for line in fhand:
    words = line.lower().split()
    for word in words:
        temp = list(word)
        for letter in temp:
            dic[letter] = dic.get(letter, 0) + 1
print(dic)
