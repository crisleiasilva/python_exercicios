#Média
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(nota1, nota2, media))
if media >= 7:
    print('Você está \033[36mAPROVADO\033[m')
elif media < 5:
    print('Você está \033[31mREPROVADO\033[m')

elif 7 > media >= 5:
    print('Você está em \033[33mRECUPERAÇÃO\033[m')
