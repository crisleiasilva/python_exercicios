#Soma todos os valores
soma = 0
cont = 0
for impar in range(1,501,2):
    if impar % 3 == 0:
        cont = cont + 1 #contador ou cont += 1
        soma = soma + impar #acumulador ou soma+= impar
print("A soma de todos os {} valores é {}".format(cont, soma))


