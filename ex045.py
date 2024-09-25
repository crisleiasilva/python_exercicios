#GAME: Pedra Papel e Tesoura
from random import randint
from time import sleep
itens = ('Pedra', 'Papel','Tesoura')
computador = randint(0,2)
print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
jogador = int(input('Qual é a sua jogada? '))
print('-=' * 11)
print('O computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=' * 11)
if computador == 0: #Computador jogou PEDRA
    if jogador == 0:
        print('\033[36mEMPATE\033[m')
    elif jogador == 1:
        print('\033[32mJOGADOR VENCE\033[m')
    elif jogador == 2:
        print('\033[33mCOMPUTADOR VENCEU\033[m')
    else:
        print('\033[m31JOGADA INVÁLIDA!\033[m')

elif computador == 1: #Computador jogou PAPEL
    if jogador == 0:
        print('\033[32mCOMPUTADOR VENCEU\033[m')
    elif jogador == 1:
        print('\033[33mEMPATE\033[m')
    elif jogador == 2:
        print('\033[35mJOGADOR VENCE\033[m')
    else:
        print('\033[31mJOGADA INVÁLIDA!\033[m')
elif computador == 2: #Computador jogou TESOURA
    if jogador == 0:
        print('\033[37mJOGADOR VENCE\033[m')
    elif jogador == 1:
        print('\033[35mCOMPUTADOR VENCE\033[m')
    elif jogador == 2:
        print('\033[36mEMPATE\033[m')
    else:
        print('\033[31mJOGADA INVÁLIDA!\033[m')
