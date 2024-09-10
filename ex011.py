#Pintando Parede

larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
area = larg * alt
print('Sua parede tem a dimensão de {} x {} e sua área é de {} m2'.format(larg, alt, area))
tinta = area / 2
print('Para pintar essa parede, você precisará de {}L de tinta.'.format(tinta))

print('A área total de parede é {} e você usará {}L de tinta para pintá-la.'.format(area,tinta ))