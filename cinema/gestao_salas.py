import json

GREEN = "\033[0;32m"
RED = "\033[1;31m"
BLUE = "\033[94m"
RESET = "\033[0;0m"  

def criar_arquivo_json():
    dados_iniciais = {"salas": []}

    with open('salas.json', 'w') as file:
        json.dump(dados_iniciais, file, indent=2)

def carregar_dados_salas(): 

    try:
        with open('salas.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        # Se o arquivo não existir, cria um novo
        criar_arquivo_json()
    return carregar_dados_salas()

salas_Data = carregar_dados_salas()

def salvar_dados_sala():
        with open('salas.json', 'w') as file:
            json.dump(salas_Data, file, indent=2)


def gestao_sala(escolha_gestor_callback):
    teste4 = 1
    while teste4 == 1:
    
        print("\n==============|| Salas ||============\n")
        escol =  int(input("1 Adicionar \n2 Consultar \n3 Excluir \n4 Voltar \n"))

        while escol  == 1:
            if escol == 1:
                print("\n")
                adicionar_Sala()
                print("\n")
                break
            else:
                print("Tente novamente")

        while escol  == 2:
            if escol == 2:
                print("\n")
                mostrar_sala()
                print("\n")
                break
            else:
                print("Tente novamente")
            
        while escol  == 3:
            if escol == 3:
                print("\n")
                excluir_sala()
                print("\n")
                break
            else:
                print("Tente novamente")
        while escol  == 4:
            if escol == 4:
                teste4 = 0
                escolha_gestor_callback()
            else:
                print("Tente novamente")

def adicionar_Sala():
    global salas_Data

    numero_sala = int(input("Digite o número da sala que deseja adicionar: "))

    # Verifica se o número da sala já existe
    if any(sala["sala"] == numero_sala for sala in salas_Data["salas"]):
        print(f"A sala {numero_sala} já existe. Escolha outro número.")
    else:
        sala = {
            "sala": numero_sala,
            "poltronas": [
                {"poltrona": i, "Ocupado": False} for i in range(1, 51)
            ]
        }
        salas_Data["salas"].append(sala)
        print("\n ---- Sala adicionada com sucesso! ---- ")
        salvar_dados_sala()

def excluir_sala():
    global salas_Data
    sala_excluir = int(input("Digite o número da sala que deseja excluir: "))

    for sala in salas_Data["salas"]:
        if sala["sala"] == sala_excluir:
            salas_Data["salas"].remove(sala)
            print("Sala excluida com sucesso!")
            salvar_dados_sala()
            break
    else:
        print("Sala não encontrada.")
    

def exibir_tabela_sala(dados_sala): 
    for poltrona in dados_sala["poltronas"]:
        numero = poltrona["poltrona"]
        ocupada = poltrona["Ocupado"]

        marcacao = RED + f"{numero}" + RESET if ocupada else GREEN + f"{numero}" + RESET

        print(f"{marcacao}\t", end="")

        if numero % 5 == 0:
            print()
    print()

def mostrar_sala():
    numero_sala = int(input("Digite o número da sala de cinema: "))

    # Carrega os dados da sala selecionada
    dados_salas = carregar_dados_salas()
    dados_sala_selecionada = None

    #print(dados_salas["salas"])


    for sala in dados_salas["salas"]:
        if sala["sala"] == numero_sala:
            dados_sala_selecionada = sala
            break

    if dados_sala_selecionada:
        print(f"\n=====================|| SALA: {dados_sala_selecionada['sala']} ||==========================\n")
        exibir_tabela_sala(dados_sala_selecionada)
        print("==============================================================================================\n")
    else:
        print(f"A sala {numero_sala} não foi encontrada.")

def ler_escrever_sala(numero_sala):
    # Carrega os dados da sala selecionada
    dados_salas = carregar_dados_salas()
    dados_sala_selecionada = None

    valor = 0
    total = 0
    
    ArraySemSalaSelecionada = []

    for sala in dados_salas["salas"]:
        if sala["sala"] == numero_sala:
            dados_sala_selecionada = sala
            break
        else:
            ArraySemSalaSelecionada.append(sala)

    if dados_sala_selecionada:
        print(f"\n=====================|| SALA: {dados_sala_selecionada['sala']} ||==========================\n")
        exibir_tabela_sala(dados_sala_selecionada)
        print("==============================================================================================\n")

        # Solicita ao usuário a quantidade de cadeiras
        quantidade_cadeiras = int(input("Digite a quantidade de cadeiras desejadas: "))

        # Solicita ao usuário as cadeiras específicas
        cadeiras_escolhidas = set()
        for _ in range(quantidade_cadeiras):
            while True:
                cadeira = int(input(f"Digite o número da cadeira {len(cadeiras_escolhidas) + 1}: "))

                # Verifica se a cadeira já está ocupada
                if not dados_sala_selecionada["poltronas"][cadeira - 1]["Ocupado"] and cadeira not in cadeiras_escolhidas:
                    cadeiras_escolhidas.add(cadeira)
                    valor = int(input(f"Digite o tipo de ingresso: (1 Inteira | 2 Meia | 3 Não pagante) \n"))
                    if valor == 1:
                        total = total + 20.00
                    elif valor == 2:
                        total = total + 10.00
                    elif valor == 3:
                        total = total + 0.00
                    break
                else:
                    print("\n !!! - Escolha inválida. Certifique-se de escolher uma cadeira disponível e que ainda não foi selecionada. - !!!\n")

        # Atualiza o arquivo JSON com as cadeiras escolhidas
        for posicao in dados_sala_selecionada["poltronas"]:
            numero_posicao = posicao["poltrona"]
            if numero_posicao in cadeiras_escolhidas:
                posicao["Ocupado"] = True


        ArraySemSalaSelecionada.append(dados_sala_selecionada)

        # Salva as alterações no arquivo JSON
        with open('salas.json', 'w') as file:
            json.dump({"salas": ArraySemSalaSelecionada}, file, indent=2)
            
        print(f"Valor Total da compra deu R${total} reais.")
        print("\nReserva efetuada com sucesso!")

        print(f"\n=====================|| SALA: {dados_sala_selecionada['sala']} ||==========================\n")
        exibir_tabela_sala(dados_sala_selecionada)
        print("==============================================================================================\n")
    else:
        print(f"A sala {numero_sala} não foi encontrada.")

