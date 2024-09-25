#Lista de Filmes
filmes = ["Filme 1", "Filme 2", "Filme 3", "Filme 4", "Filme 5"]
print("Bem-vindo à classificação de filmes!")
print("Você tem cinco filmes para classificar")
print("Digite '0' a qualquer momento para encerrar.\n")
#Loop para interagir com caca filme na lista
for filme in filmes:
    classificacao = input("Como você classificaria '(filme)' de 1 a 5? (ou 0 para parar)")
    if classificacao == '0':
        print("Que pena você não irá classificar os filmes")
        break
    classificacao = int(classificacao)
    if classificacao < 1 or classificacao > 5:
        print("Por favor, digite uma classificação válida de 1 a 5.")
    else:
        print(f"Você classificou '(filme)'com {classificacao} estrelas.\n ")
print("Obrigado por classificar os filmes!")