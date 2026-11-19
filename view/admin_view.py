from services.loja_services import create_games, list_games, delete_game, update_game, cadastrar_desenvolvedora, listar_desenvolvedoras, deletar_desenvolvedora, atualizar_desenvolvedora, gerenciar_usuarios
from services.user_services import insert_admin
from os import system #system cls
from msvcrt import getch


def admin_panel(user_auth):
    while True:
        print(f"Bem vindo {user_auth[1]}")
        print("1 - Desenvolvedoras")
        print("2 - Jogos")
        print("3 - Gerenciar usuários")
        print("4 - Criar admin")
        print("5 - Deslogar")

        opc = int(input("Digite uma opção: "))

        if opc == 1:
            while True:
                print("1 - Cadastrar desenvolvedora")
                print("2 - Listar desenvolvedoras")
                print("3 - Remover desenvolvedora")
                print("4 - Atualizar desenvolvedora")
                print("5 - Voltar ao menu do admin")

                opc_dev = int(input("Digite uma opção: "))

                match opc_dev:
                    case 1:
                        nome = input("Digite o nome da desenvolvedora: ")
                        CEP = input("Digite o CEP da desenvolvedora: ")
                        CNPJ = input("Digite o CNPJ da desenvolvedora: ")
                        cadastrar_desenvolvedora(nome, CEP, CNPJ)
                        print("Pressione uma tecla para continuar...")
                        getch()
                    case 2:
                        desenvolvedoras = listar_desenvolvedoras()
                        for dev in desenvolvedoras:
                            print(f"Desenvolvedoras: ID: {dev[0]} - Nome: {dev[1]} - CEP: {dev[2]} - {dev[3]}")
                            print("Pressione uma tecla para continuar...")
                            getch()
                    case 3:
                        id_dev = int(input("Digite o id da desenvolvedora para remover: "))
                        deletar_desenvolvedora(id_dev)
                        print("Pressione uma tecla para continuar...")
                        getch()
                    case 4:
                        id_dev = int(input("Digite o id da desenvolvedora para atualizar: "))
                        nome = input("Digite o novo nome da desenvolvedora: ")
                        CEP = input("Digite o novo CEP da desenvolvedora: ")
                        CNPJ = input("Digite o novo CNPJ da desenvolvedora: ")
                        atualizar_desenvolvedora(id_dev, nome, CEP, CNPJ)
                        print("Pressione uma tecla para continuar...")
                        getch()
                    case 5:
                        break
                    case _:
                        print("Digite uma opção válida!")
                    
        elif opc == 2:
            while True:
                print("1 - Cadastrar jogo")
                print("2 - Listar jogos")
                print("3 - Remover jogo")
                print("4 - Atualizar jogo")
                print("5 - Voltar ao menu do admin")
                opc_game = int(input("Digite uma opção: "))
                match opc_game:
                    case 1:
                        nome = input("Digite o nome do jogo: ")
                        valor = float(input("Digite o valor do jogo: "))
                        data_lacamento = input("Digite a data de lançamento do jogo (YYYY-MM-DD): ")
                        genero = input("Digite o gênero do jogo: ")
                        tamanho = float(input("Digite o tamanho do jogo (em GB): "))
                        dev_id = int(input("Digite o ID da desenvolvedora: "))
                        create_games(nome, valor, data_lacamento, genero, tamanho, dev_id)
                        print("Pressione uma tecla para continuar...")
                        getch()
                    case 2:
                        jogos = list_games()
                        for game in jogos:
                            print(f"Jogos: ID: {game[0]} - Nome: {game[1]} - Valor: {game[2]} - Data de Lançamento: {game[3]} - Gênero: {game[4]} - Tamanho: {game[5]} - Desenvolvedora ID: {game[6]}")
                            print("Pressione uma tecla para continuar...")
                            getch()
                    case 3:
                        id_game = int(input("Digite o id do jogo para remover: "))
                        delete_game(id_game)
                        print("Pressione uma tecla para continuar...")
                        getch()
                    case 4:
                        id_game = int(input("Digite o id do jogo para atualizar: "))
                        nome = input("Digite o novo nome do jogo: ")
                        valor = float(input("Digite o novo valor do jogo: "))
                        data_lacamento = input("Digite a nova data de lançamento do jogo (YYYY-MM-DD): ")
                        genero = input("Digite o novo gênero do jogo: ")
                        tamanho = float(input("Digite o novo tamanho do jogo (em GB): "))
                        dev_id = int(input("Digite o novo ID da desenvolvedora: "))
                        update_game(id_game, nome, valor, data_lacamento, genero, tamanho, dev_id)
                        print("Pressione uma tecla para continuar...")
                        getch()
                    case 5:
                        break
                    case _:
                        print("Digite uma opção válida!")

        elif opc == 3:
            gerenciar_usuarios()

        elif opc == 4:
            nome = input("Digite o nome do admin: ")
            email = input("Digite o email do admin: ")
            cpf = input("Digite o CPF do admin: ")
            endereco = input("Digite o endereço do admin: ")
            senha = input("Digite a senha do admin: ")
            insert_admin(nome, email, cpf, endereco, senha)
            print("Admin cadastrado com sucesso!")

        elif opc == 5:
            system('cls')
            break

        else:
            print("Digite uma opção válida!")
