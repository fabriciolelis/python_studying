print('-=-' * 10)
print('Vamos Analisar Triângulos...')
print('-=-' * 10)
p1 = float(input('Primeiro segmento: '))
p2 = float(input('Segundo segmento: '))
p3 = float(input('Terceiro segmento: '))

if (abs(p2 - p3) < p1 < p2 + p3) and (abs(p1 - p3) < p2 < p1 + p3) and (abs(p1 - p2) < p3 < p1 + p2):
    if (p1 == p2) and (p2 == p3):
        print('Os segmentos acima PODEM FORMAR um triângulo EQUILÁTERO')
    elif (p1 != p2) and (p1 != p3) and (p2 != p3):
        print('Os segmentos PODEM FORMAR formar um triângulo ESCALENO')
    else:
        print('Os segmentos acima PODEM FORMAR um triagulo ISÓSCELES!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo!')
