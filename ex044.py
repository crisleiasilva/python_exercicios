#Gerenciador de Pagamentos
print('{:=^40}'.format(' LOJAS MIG '))
compra = float(input('Valor da Compra: R$'))
print('''FORMAS DE PAGAMENTO 
[1] à vista dinheiro/PIX
[2] á vista cartão
[3] 2x no cartão
[4] 3 x ou mais no cartão''')
opcao = int(input('Qual é a opção? '))
if opcao == 1:
    total = compra - (compra * 10 /100)
elif opcao == 2:
    total = compra - (compra * 5 / 100)
elif opcao == 3:
    total = compra
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R$ {:.2f} SEM JUROS'.format(parcela))
elif opcao == 4:
    total = compra + (compra * 20 / 100)
    totalparc = int(input('Quantas parcelas? '))
    parcela = total / totalparc
    print('Sua compra será parcela em {}x de R$ {:.2f} COM JUROS'.format(totalparc, parcela))
else:
    total = compra
    print('\033[31mOPÇÃO INVÁLIDA DE PAGAMENTO!\033[m')
print('Sua compra de R$ {:.2f} vai custar R$ {:.2f} no final'.format(compra,total))
