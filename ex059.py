#Criando um Menu de Opções
from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print('''    [1] somar
    [2] multiplicar
    [3] maior
    [4]novos números
    [5] sair do programa''')
    opcao = int(input('>>>>>Qual é a sua opção? '))
    if opcao == 1:
        soma = n1 + n2
        print('A soma entre {} + {} é {}'.format(n1,n2, soma))
        print("=-=" * 10)
    elif opcao == 2:
        produto = n1 * n2
        print('O resultado de {} x {} é {}'.format(n1,n2,produto))
        print('=-=' * 10)
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior valor é {}'.format(n1,n2,maior))
        print('=-=' *10)
    elif opcao == 4:
        print('Informe os números novamente: ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
        print('=-=' *10)
    elif opcao == 5:
        print('Finalizando....')
        print('=-=' * 10)
    else:
        print('Opção inválida. Tente novamente!')
        print('=-=' * 10)
        sleep(2)

print('Fim do programa! Volte sempre!')