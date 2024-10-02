'''def somar(a, b):
    return a + b

def subtrair(a,b):
    return a - b

def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado da operação {a} + {b} = {resultado}")

exibir_resultado(10,10, somar)
exibir_resultado(10,10, subtrair)

op = somar
print(op(1,23))'''

salario = 5000

def salario_bonus(bonus):
    global salario
    salario += bonus
    return salario

novo_salario = salario_bonus(500)
print(novo_salario)
