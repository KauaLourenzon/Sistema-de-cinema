import json

def cria_Json_Funcionario():
    jsonFuncionarios = {"funcionarios": []}

    with open('funcionarios.json', 'w') as file2:
        json.dump(jsonFuncionarios, file2, indent=2)

# Função para carregar os dados do arquivo JSON
def carregar_Dados_Funcionario():
    try:
        with open('funcionarios.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        # Se o arquivo não existir, cria um novo
        cria_Json_Funcionario()
        return carregar_Dados_Funcionario()

def salvar_Dados_Funcionario():
    with open('funcionarios.json', 'w') as file:
        json.dump(funcionarios_data, file, indent=2)

funcionarios_data = carregar_Dados_Funcionario()

def gestao_fun(escolha_gestor_callback):
    teste3 = 1
    while teste3 == 1:
        print("\n=====================|| GESTÃO DE FUNCIONARIOS ||====================\n")
        esco = int(input("1 Adicionar \n2 Consultar \n3 Excluir \n4 Voltar \n\nEscolha: "))

        if esco == 1:
            print("\n")
            adicionar_Funcionario()
            print("\n")

        elif esco == 2:
            print("\n")
            mostrar_funcionario()
            print("\n")

        elif esco == 3:
            print("\n")
            excluir_Funcionario()
            print("\n")

        elif esco == 4:
            teste3 = 0
            # Salva as alterações no arquivo JSON antes de sair
            with open('funcionarios.json', 'w') as file:
                json.dump(funcionarios_data, file, indent=2)

            escolha_gestor_callback()

        else:
            print("Opção inválida. Tente novamente.")

def adicionar_Funcionario():
    global funcionarios_data

    
    while True:
        nome = input("Digite o nome do funcionário: ")
        rg = input("Digite o RG do novo funcionário (apenas números): ")
        horario_entrada = input("Digite o horário de entrada do novo funcionário (por exemplo 00:00): ")
        horario_saida = input("Digite o horário de saída do funcionário (por exemplo 00:00): ")
        usuario = input("Crie um login para o funcionário: ")
        senha = input("Crie a senha para o funcionário: ")

        if not rg.isdigit():
            print("!! - O RG deve conter apenas números. Tente novamente. - !!")
        elif not all(char.isdigit() or char == ':' for char in horario_entrada):
            print("!! - O horário deve conter apenas números e o caractere ':'. Tente novamente. - !!")
        elif not all(char.isdigit() or char == ':' for char in horario_saida):
            print("!! - O horário deve conter apenas números e o caractere ':'. Tente novamente. - !!")
        elif not nome.isalpha:
            print("!! - O nome deve conter apenas letras - !!")
        else:
            break


    novo_funcionario = {
        "rg": rg,
        "nome": nome,
        "horario_entrada": horario_entrada,
        "horario_saida": horario_saida,
        "usuario": usuario,
        "senha": senha
    }

    funcionarios_data["funcionarios"].append(novo_funcionario)
    print("\n ---- Funcionário adicionado com sucesso! ---- ")
    salvar_Dados_Funcionario()

def mostrar_funcionario():
    global funcionarios_data
    opcao = int(input("Escolha uma opção: \n1 Ver todos os funcionários \n2 Ver um funcionário específico \n\nEscolha: "))
    print("====================|| FUNCIONÁRIOS ||==================")

    if opcao == 1:
        if not funcionarios_data["funcionarios"]:
            print("!!! - Nenhum funcionário cadastrado. - !!!")
        else:
            for i, funcionario in enumerate(funcionarios_data["funcionarios"], 1):
                print(f"{i} - {funcionario['nome']} (RG: {funcionario['rg']})")

    elif opcao == 2:
        rg_busca = input("Digite o RG do funcionário que deseja ver: ")
        for funcionario in funcionarios_data["funcionarios"]:
            if funcionario["rg"] == rg_busca:
                detalhes_funcionario(funcionario)
                break
        else:
            print("Funcionário não encontrado.")

    else:
        print("Opção inválida. Tente novamente.")



def detalhes_funcionario(funcionario):
    print("\nDetalhes do Funcionário:")
    print(f"Nome: {funcionario['nome']}")
    print(f"RG: {funcionario['rg']}")
    print(f"Horário de Entrada: {funcionario['horario_entrada']}")
    print(f"Horário de Saída: {funcionario['horario_saida']}")
    print(f"Usuário: {funcionario['usuario']}")
    print(f"Senha: {funcionario['senha']}")

def excluir_Funcionario():
    global funcionarios_data
    rg_excluir = input("Digite o RG do funcionário que deseja excluir: ")

    for funcionario in funcionarios_data["funcionarios"]:
        if funcionario["rg"] == rg_excluir:
            funcionarios_data["funcionarios"].remove(funcionario)
            print("------- Funcionário excluído com sucesso! --------")
            salvar_Dados_Funcionario()
            break
    else:
        print("Funcionário não encontrado.")

# Carrega os dados do arquivo JSON ao iniciar o programa
funcionarios_data = carregar_Dados_Funcionario()