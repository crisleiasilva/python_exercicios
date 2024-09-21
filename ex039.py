#Alistamento Militar
from datetime import date
atual = date.today().year
ano = int(input('Ano de Nascimento: '))
idade = atual - ano
print('Quem nasceu em {} tem {} anos em {}'.format(ano,idade,atual))
if idade == 18:
    print('Você deve se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos para o alistamento'.format(saldo))
    alis = atual + saldo
    print('Seu alistamento será em {}'.format(alis))
elif idade > 18:
    saldo = idade - 18
    print('Você já deveria ter se alistado há {} anos.'.format(saldo))
    alis = atual - saldo
    print('Seu alistamento foi em {}'.format(alis))

