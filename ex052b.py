#Estruturas de repetição
'''texto = input("Informe um texto: ")
VOGAIS = "AEIOU"
for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
print()'''
#FOR
'''for numero in range(0,11):
    print(numero, end=' ')'''

#WHILE
opcao = -1

while opcao != 0: #enquanto a opção for diferente de 1 e 2 executa o código
    opcao = int(input("[1] Sacar \n[2] Extrato \n[0]Sair \n"))

    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print("Exibindo extrato...")
    else:
        print("Obrigado por usar nosso sistema, até logo!")


#BREAK
while True:
    numero = int(input("Informe um número: "))
    if numero == 10:
        break

    print(numero)