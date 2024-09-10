#Conversor de Moeda

real = float(input('Qual a quantia em dinheiro você tem na carteira: R$ '))
#dolar = real / 5.60
#print('Com R${:.2f} você pode comprar US${:.2f}'.format(real,dolar))
euro = real / 6.18
print('Com R$ {:.2f} você pode comprar EUR {:.2f}'.format(real, euro))