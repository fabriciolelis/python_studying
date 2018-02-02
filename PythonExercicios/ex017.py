from math import hypot

cat1 = float(input('Digite o valor do cateto oposto: '))
cat2 = float(input('Digite o valor do cateto adjacente: '))
print('Um triângulo com cateto oposto {} e cateto adjacente {} tem como hipotenusa {}'.format(cat1, cat2,
                                                                                             hypot(cat1, cat2)))
