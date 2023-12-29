import json
from gestao_filmes import carregar_dados_filmes, mostrar_filmes, filmes_data
from gestao_salas import ler_escrever_sala

def compra_ingresso(login_callback):
    total = 0
    print("================|| FILMES EM CARTAZ ||================== \n")
    mostrar_filmes(Buying=True)
    print("\n")

    nome_filme = input("Digite o nome do filme: ")

    # Encontrar o filme pelo nome
    filme_selecionado = None

    for filme in filmes_data["filmes"]:
        if filme["titulo"].lower() == nome_filme.lower():
            filme_selecionado = filme
            break
    
    if filme_selecionado:
        ler_escrever_sala(int(filme_selecionado["sala_disponivel"]))
        login_callback()
    else:
        print("Filme não encontrado.")
        login_callback()