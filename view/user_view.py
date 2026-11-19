from services.loja_services import list_games, add_game_to_cart
from os import system #system cls
from msvcrt import getch

def user_panel(user_auth):
    while True:
        print(f"Bem vindo {user_auth[1]}")
        print("1 - Listar jogos")
        print("2 - Adicionar jogos ao carrinho")
        print("3 - Deslogar")

        opc = int(input("Digite uma opção: "))

        match opc:
            case 1:
                jogos = list_games()
                for game in jogos:
                    print(f"Jogos: {game[0]} - {game[1]} - {game[2]} - {game[3]} - {game[4]} - {game[5]} - {game[6]}")
                    print("Pressione uma tecla para continuar...")
                    getch()
            case 2:
                game_name = input("Digite o nome do jogo que deseja adicionar ao carrinho: ")
                carrinho = add_game_to_cart(user_auth[0], game_name)
                print("Jogo adicionado ao carrinho!")
            case 3:
                system('cls')
                break
            case _:
                print("Digite uma opção válida!")
    