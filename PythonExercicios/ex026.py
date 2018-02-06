frase = str(input('Digite uma frase: ')).strip()
total = frase.lower().count('a')
first = frase.lower().find('a') + 1
last = frase.lower().rfind('a') + 1
print('A letra "a" aparece {} vezes, a primeira em {} e a última em {}'.format(total, first, last))
