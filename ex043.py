#Indice de Massa Corpórea
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura ** 2)
print('Seu IMC é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está \033[43m ABAIXO\033[m do peso normal')
elif imc >= 18.5 and imc < 25:
    print('Você está no peso \033[43mNORMAL\033[m')
elif imc >= 25 and imc < 30:
    print('Você está com \033[43mSOBREPESO\033[m')
elif imc < 30 and imc <=40:
    print('Você está com \033[43mOBESIDADE\033[m')
else:
    print('Você está com \033[43mOBESIDADE MÓRBIDA\033[m')
