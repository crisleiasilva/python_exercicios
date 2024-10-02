#Funções
'''def salvar_carro(marca, modelo, ano, placa):
    #salva carro no banco de dados
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")

salvar_carro("Chery", "Tiggo", 2024, "ABC-1234")
salvar_carro(marca= "Chery", modelo= "Tiggo", ano= 2024, placa= "ABC-1234")
salvar_carro(**{"marca": "Chery", "modelo": "Tiggo", "ano": 2024, "placa":"ABC-1234"})'''

'''*args e **kwargs: combinação de parâmetros obrigatórios, quando são definidos
o método recebe os valores como tupla e dicionário respectivamente.'''

def exibir_poema(data_extenso, *args, **kwargs):
    texto = "\n".join(args)
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)

exibir_poema("Sábado, 28 de Setembro de 2024","Zen of Python", "Beautiful is better than ugly.", autor= "Tim Peters", ano=1999)


def criar_carro(modelo, ano, placa, / ,marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro("Tiggo", 2024, "ABC-1234", marca="Chery", motor="2.0", combustivel="Flex")
