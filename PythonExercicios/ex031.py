dist = float(input('Qual a distância da sua viagem: '))
if dist <= 200:
    print('Sua viagem de {}Km vai custar R${:.2f}'.format(dist, dist * 0.5))
else:
    print('Sua viagem de {}Km vai custar R${:.2f}'.format(dist, dist * 0.45))
