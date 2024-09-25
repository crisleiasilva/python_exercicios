#Estrutura de Repetição: For
'''numeros = [1,2,3,4,5]
for num in numeros:
    print(num)'''

#Estrutura Repetição: While
numero = int(input('Digite um número(ou 0 para sair): '))
while numero != 0:
    if numero % 2 == 0:
        print('O número é PAR')
        break
    else:
        print('O número é ÍMPAR')
        break
numero = int(input('Digite outro número(ou 0 para sair): '))


#Controles de Repetição: Range, break, continue
'''for x in range(5):
    print(x)
for y in range(2,7):
    print(y)
for z in range(1,11,2):
    print(2)'''

'''for numero in range(1,11):
    if numero % 2 == 0:
        print('O primeiro número par encontrado é: ', numero)
        break'''

for numero in range(1,11):
    if numero == 5:
        continue
        print(numero)