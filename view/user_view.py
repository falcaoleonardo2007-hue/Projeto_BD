from services.loja_services import list_games, add_game_to_cart, list_cart_games, remove_game_from_cart, list_games_com_dev
from os import system #system cls
from msvcrt import getch

def user_panel(user_auth):
    while True:
        print(f"Bem vindo {user_auth[1]}")
        print("1 - Listar jogos")
        print("2 - Adicionar jogos ao carrinho")
        print("3 - Carrinho")
        print("4 - Deslogar")

        try:
            opc = int(input("Digite uma opção: "))
            system('cls')
        except ValueError:
            print("Digite um número válido!")
            continue

        match opc:
            case 1:
                opc = int(input("1 - Listar todos os jogos\n2 - Listar jogos com desenvolvedora\nDigite uma opção: "))
                if opc == 1:
                    print("--JOGOS--")
                    jogos = list_games()
                elif opc == 2:
                    print("--JOGOS--")
                    jogos = list_games_com_dev()
                for game in jogos:
                    print(f"Jogos: ID_Jogo: {game[0]} - ID_Dev: {game[1]} - Nome: {game[2]} - Preço:{game[3]} reais - Lançamento:{game[4]} - Gênero: {game[5]} - Tamanhp: {game[6]}")
                    print("Pressione uma tecla para continuar...")
                    getch()
            case 2:
                jogos = list_games()
                for game in jogos:
                    print(f"Jogos: {game[2]} | Preço: R$ {game[3]}") 

                game_name = input("Digite o nome do jogo que deseja adicionar ao carrinho: ")
                carrinho = add_game_to_cart(user_auth[0], game_name)
                if carrinho is not None:
                    print("Jogo adicionado ao carrinho!")
            case 3:
                while True:
                    print("Selecione uma opção:")
                    print("1 - Mostrar carrinho")
                    print("2 - Remover jogo")
                    print("3 - Voltar")
                    try:
                        opc = int(input("Digite uma opção: "))
                        system('cls')
                    except ValueError:
                        print("Digite um número válido!")
                        continue
                    match opc:
                        case 1:
                            print("--SEU CARRINHO--")
                            jogos = list_cart_games(user_auth[0])
                            if not jogos:
                                print("Carrinho vazio!")
                            else:
                                for game in jogos:
                                    print(f"Jogo: {game[0]} | Preço: R$ {game[1]:.2f}")
                        case 2:
                            print("--SEU CARRINHO--")
                            jogos = list_cart_games(user_auth[0])
                            for game in jogos:
                                print(f"Jogo: {game[2]}")

                            game_name = input("Digite o nome do jogo que deseja remover: ")
                            remove_game_from_cart(user_auth,game_name)

                        case 3:
                            break
                        case _:
                            print("Digite uma opção válida!")
            case 4:
                system('cls')
                break
            case _:
                print("Digite uma opção válida!")
    