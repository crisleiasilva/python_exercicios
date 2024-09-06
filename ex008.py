#Conversor de medidas

medida = float(input('Digite uma distância em metros: '))
cm = medida * 100
mm = medida * 1000
km = medida / 1000
print('A medida de {}m corresponde a {:.0f}cm , {:.0f}mm e {}km '.format(medida, cm, mm, km))