#Empréstimo Bancário
casa = float(input('Valor do imóvel:R$ '))
salario = float(input('Salário co Comprador: R$ '))
anos = int(input('Quantos anos de financiamento: '))
prestacao = casa / (anos * 12)
minimo = salario * 30 /100
print('\033[31;40mPara comprar um imóvel de R${:.2f} em {} anos a prestação será de R${:.2f}\033[m'.format(casa,anos,prestacao))
if prestacao <= minimo:
    print('Empréstimo \033[31mAPROVADO!\033[m')
else:
    print('Empréstimo \033[31mNEGADO!\33[m')