#Par ou ímpar
num = int(input('Digite um número: '))
res = num % 2
if res == 0:
    print('Você digitou o número {} e ele é PAR'.format(num))
else:
    print('Você digitou o número {} e ele é ÍMPAR'.format(num))
