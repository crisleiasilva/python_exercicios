'''Catetos e Hipotenusa'''


#ex sem importação
'''co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hi))'''

#ex com importação
from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento cateto adjacente: '))
hi = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))

