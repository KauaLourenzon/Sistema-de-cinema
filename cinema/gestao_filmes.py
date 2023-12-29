import json
from gestao_salas import carregar_dados_salas

def cria_json_filmes():
    json_filmes = {"filmes": []}

    with open('filmes.json', 'w') as file2:
        json.dump(json_filmes, file2, indent=2)

def carregar_dados_filmes():
    try:
        with open('filmes.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        cria_json_filmes()
        return carregar_dados_filmes()

def salvar_dados_filmes():
    with open('filmes.json', 'w') as file:
        json.dump(filmes_data, file, indent=2)

filmes_data = carregar_dados_filmes()

def gestao_filmes(escolha_gestor_callback):
    teste2 = 1
    while teste2 == 1:
        print("\n================|| GESTÃO DE FILMES ||==================\n")
        esc = int(input("\nEscolha uma Opção:\n1 Adicionar \n2 Consultar \n3 Excluir \n4 Voltar \n\nEscolha: "))

        while esc == 1:
            if esc == 1:
                print("\n")
                adicionar_filmes()
                print("\n")
                break
            else:
                print("Tente novamente")

        while esc == 2:
            if esc == 2:
                print("\n")
                mostrar_filmes(Buying=False)
                print("\n")
                break
            else:
                print("Tente novamente")

        while esc == 3:
            if esc == 3:
                print("\n")
                remocao_de_filmes()
                print("\n")
                break
            else:
                print("Tente novamente")
        while esc == 4:
            if esc == 4:
                teste2 = 0
                escolha_gestor_callback()
            else:
                print("Tente novamente")

def adicionar_filmes():
    global filmes_data

    novo_filme = {
        "titulo": input("Digite o título do filme: "),
        "genero": input("Digite o gênero do filme: "),
        "classificacao": input("Digite a classificação do filme: "),
        "sala_disponivel": None
    }

    sala_filme = int(input("Digite o número da sala disponível: ").strip())

    # Verifica se a sala existe no arquivo de salas
    salas_existentes = carregar_dados_salas()["salas"]
    sala_numero = sala_filme
    
    # Verifica se a sala já foi adicionada ao filme
    if any(filme["sala_disponivel"] == sala_numero for filme in filmes_data["filmes"]):
        print(f"\n!! - A sala {sala_numero} já foi adicionada a outro filme. Escolha outra sala. - !!")
    elif any(sala["sala"] == sala_numero for sala in salas_existentes):
        novo_filme["sala_disponivel"] = sala_numero
        filmes_data["filmes"].append(novo_filme)
        print("\n ---- Filme adicionado com sucesso! ---- ")
    else:
        print(f"\n!! - A sala {sala_numero} não existe. Por favor, verifique se há salas cadastradas e escolha uma sala existente. - !!")

    salvar_dados_filmes()


def mostrar_filmes(Buying: bool):
    global filmes_data
    if Buying == False:
        opcao = int(input("Escolha uma opção: \n1 Ver todos os filmes \n2 Ver um filme específico \n\nEscolha: "))
        print("====================|| FILMES ||==================")

        if opcao == 1:
            if not filmes_data["filmes"]:
                print("!!! - Nenhum filme cadastrado. - !!!")
            else:
                for i, filme in enumerate(filmes_data["filmes"], 1):
                    sala_disponivel = filme['sala_disponivel']
                    print(f"{i} - {filme['titulo']} - Sala: {sala_disponivel}")
        elif opcao == 2:
            titulo_busca = input("Digite o título do filme: ")
            for filme in filmes_data["filmes"]:
                if filme["titulo"] == titulo_busca:
                    detalhes_filme(filme)
                    break
                else:
                    print("O Filme não foi encontrado.")
        else:
            print("Opção Inválida!")
    else:
            if not filmes_data["filmes"]:
                print("!!! - Nenhum filme cadastrado. - !!!")
            else:
                for i, filme in enumerate(filmes_data["filmes"], 1):
                    sala_disponivel = filme['sala_disponivel']
                    print(f"{i} - {filme['titulo']} - Sala: {sala_disponivel}")

def detalhes_filme(filme):
    print("\nDetalhes do Filme:")
    print(f"Título: {filme['titulo']}")
    print(f"Gênero: {filme['genero']}")
    print(f"Classificação: {filme['classificacao']}")
    
    # Verifica se a chave 'sala_disponivel' existe no dicionário
    if 'sala_disponivel' in filme:
        print(f"Sala Disponível: {filme['sala_disponivel']}")
    else:
        print("Sala Disponível: Não informada")

def remocao_de_filmes():
    global filmes_data
    titulo_excluir = input("Digite o título do filme que deseja excluir: ")

    for filme in filmes_data["filmes"]:
        if filme["titulo"] == titulo_excluir:
            filmes_data["filmes"].remove(filme)
            print("\n------ Filme excluído com sucesso! -------")
            salvar_dados_filmes()
            break
    else:
        print("Filme não encontrado.")
