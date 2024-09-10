#Reajuste de salário
#salario = float(input('Qual é o salário do Funcionário? R$'))
#aumento = salario + (salario * 15 /100)
#print('Seu salário atual é de R${:.2f} com o reajuste de 15% será de R${:.2f}'.format(salario,aumento))

valorProduto =float(input('Qual o valor do produto: R$'))
avista = valorProduto - (valorProduto * 5 /100)
parcelado = valorProduto + (valorProduto * 8 /100)
print('O valor do produto é R$ {:.2f}'.format(valorProduto))
print('Pagamento à vista valor do produto será R${:.2f}'.format(avista))
print('Pagamento parcelado valor do produto será R${:.2f}'.format(parcelado))
