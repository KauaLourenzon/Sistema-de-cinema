import json
import os
import re
import sys

from gestao_funcionarios import gestao_fun
from gestao_filmes import gestao_filmes, carregar_dados_filmes
from gestao_salas import gestao_sala
from compra_ingressos import compra_ingresso

GREEN = "\033[0;32m"
RED = "\033[1;31m"
BLUE = "\033[94m"
RESET = "\033[0;0m"

def criar_Jsons():
    jsonFilmes = {"filmes": []}
    jsonSalas = {"salas": []}

    with open('filmes.json', 'w') as file:
        json.dump(jsonFilmes, file, indent=2)


    with open('salas.json', 'w') as file3:
        json.dump(jsonSalas, file3, indent=2)

def login():
    fim = True
    G_user = "gestor"
    G_senha = "gestor"

    A_user = "atendente"
    A_senha = "atendente"

    while True:
        print("==============|| LOGIN ||================")
        usuario =  int(input("1 Gestor \n2 Atendente \n3 Desligar \nEscolha: "))

        if usuario == 1 or usuario == 2:
            while True:
                User = (input("Digite o usuário: "))
                senha=(input("Digite a senha: "))

                if usuario == 1 and senha == G_senha and User == G_user:
                    print("\n" + BLUE + "Login Realizado com sucesso")
                    print(RESET)
                    Escolha_gestor()
                    break
                elif usuario == 2 and senha == A_senha and User == A_user:
                    print("\n" + BLUE + "Login Realizado com sucesso")
                    print(RESET) 
                    print("boa compra")
                                 
                    compra_ingresso(login)
                    break
                else:
                    print("Senha ou usuário incorreto!")
            break
        elif usuario == 3:
            exit()
        else:
            print("opção invalida")

def Escolha_gestor():
    teste1 = 1
    while teste1 == 1:
        print("================|| GERENCIAMENTO DO CINEMA ||=================\n")
        esc =  int(input("\n1 Manutenção Funcionario \n2 Manutenção Filmes \n3 Manutenção Sala\n4 Encerrar Login\n\nEscolha: "))

        while esc  == 1:
            if esc == 1:
                gestao_fun(Escolha_gestor)
                break
            else:
                print("Tente novamente")

        while esc  == 2:
            if esc == 2:
                gestao_filmes(Escolha_gestor)
                break
            else:
                print("Tente novamente")
            
        while esc  == 3:
            if esc == 3:
                gestao_sala(Escolha_gestor)
                break
            else:
                print("Tente novamente")
                
        while esc  == 4:
            if esc == 4:
                print(BLUE + "Login encerrado!")
                print(RESET)
                return login()
                break
            else:
                print("Tente novamente")

login()