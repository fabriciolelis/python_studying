vel = float(input('Qual é a velocidade atual do carro? '))

if vel > 80:
    print('Você foi multado!!! A multa vai custar R${:.2f}'.format((vel - 80) * 7))
else:
    print('Continue assim!!! Tenha um bom dia!!')
