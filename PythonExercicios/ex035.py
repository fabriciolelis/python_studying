print('-=-' * 10)
print('Vamos Analisar Triângulos...')
print('-=-' * 10)
p1 = float(input('Primeiro segmento: '))
p2 = float(input('Segundo segmento: '))
p3 = float(input('Terceiro segmento: '))

if (abs(p2 - p3) < p1 < p2 + p3) and (abs(p1 - p3) < p2 < p1 + p3) and (abs(p1 - p2) < p3 < p1 + p2):
    print('Os segmentos acima PODEM FORMAR um triagulo!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo!')
