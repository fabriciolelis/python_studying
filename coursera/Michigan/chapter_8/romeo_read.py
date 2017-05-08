fname = 'romeo.txt'
fhand = open(fname)

final_list = []

for line in fhand:
    line = line.rstrip()
    phrase = line.split()
    for word in phrase:
        if word not in final_list:
            final_list.append(word)
final_list.sort()
print(final_list)

