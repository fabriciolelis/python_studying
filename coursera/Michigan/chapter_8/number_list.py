numlist = list()
while True:
    inp = input('Enter a number: ')
    if inp == 'done':
        break
    value = float(inp)
    numlist.append(value)

print('Maximum: ', max(numlist))
print('Minimum: ', min(numlist))
