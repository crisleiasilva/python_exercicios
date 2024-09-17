#Multa de trânsito
vel = float(input('Digite sua velocidade no trecho anterior: '))
mul = vel * 7
if vel >=80:
    print('Sua velocidade foi de {} km/h e você será MULTADO'.format(vel))
else:
    print('Boa viagem, dirija com cinto de segurança')
