'''Funções: bloco de código identificado por um nome e pode receber uma lista
de parâmetros, esses parâmetros podem ou não ter valores
padrões. Torna o código mais legível e possibilita o reaproveitamento
É programar de maneira estruturada.'''

'''def exibir_mensagem(): #def é usado para informar que não é variável
    print("\033[35mOlá Mundo\033[m!!!")

def exibir_mensagem_2(nome):
    print(f"Seja bem vindo {nome}!")

def exibir_mensagem_3(nome= "Anônimo"):
    print(f"Seja bem vindo {nome}!")

exibir_mensagem()
exibir_mensagem_2(nome= "Miguel")
exibir_mensagem_3()
exibir_mensagem_3(nome= "Crislei")'''

def calcular_total(numeros):
    return sum(numeros)

def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1

    return antecessor, sucessor

def func_3():
    print("Olá Mundo!")
    return None

print(calcular_total([10, 20, 34]))
print(retorna_antecessor_e_sucessor(10))
print(func_3())