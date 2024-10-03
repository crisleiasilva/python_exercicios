#Jogo de Adivinhação
from random import randint
computador = randint(0,10)
print('Sou seu computador.... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi? ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('\033[31mMais... Tente mais uma vez!\033[m')
        elif jogador > computador:
            print('\033[31mMenos... Tente mais uma vez!\033[m')
print('Acertou com \033[34m{} tentativas\033[m!!!'.format(palpites))