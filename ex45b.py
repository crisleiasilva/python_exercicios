#Praticando estruturas condicionais
#saldo = 2000.0
'''saque = float(input('Informe o valor do saque: '))

if saldo >= saque:
    print("Realizando saque!")
else:
    print("Saldo insuficiente!")

# Praticando...
opcao = int(input("Informe uma opção: [1] Sacar \n[2] Extrato: "))
if opcao == 1:
    valor = float(input("Informe a quantia para o saque: "))
elif opcao == 2:
    print("Exibindo extrato...")
else:
    print("Opção inválida")'''

#if/elif/else
conta_normal = True
conta_universitaria = False
saldo = 2000
saque = 2500
cheque_especial = 450

if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com uso do cheque especial")
    else:
        print("Não foi possível realizar o saque")
elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    else:
        print("Saldo insuficiente")