#Calculando desconto
preco = float(input('Qual é o preço do produto? R$'))
promo = preco - (preco *5 /100)
print('O valor do produto é R$ {:.2f} e com o desconto da promoção você pagará R$ {:.2f}'.format(preco, promo))