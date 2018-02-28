num = int(input('Digite um número: '))
count = 0
for i in range(1, num + 1):
    if num % i == 0:
        count += 1
print('O número {} foi divisível {} vezes'.format(num, count))
if count > 2:
    print('E por isso ele NÃO É PRIMO')
else:
    print('E por isso ele é um NÚMERO PRIMO')
