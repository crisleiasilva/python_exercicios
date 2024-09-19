#Comparando Números
a = int(input('Primeiro número: '))
b = int(input('Segundo número: '))
if a > b:
    print('O \033[41mPRIMEIRO\033[m número é maior')
elif b > a:
    print('O \033[41mSEGUNDO\033[m número é maior')
else:
    print('Os valores são \033[43mIGUAIS\033[m')


