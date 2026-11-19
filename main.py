from services.user_services import insert_cliente, login, validar_admin
from view.admin_view import admin_panel
from view.user_view import user_panel
import pwinput
from validacoes.regex import validar_email
from os import system #system cls
from msvcrt import getch #getch() - Pressionar tecla para continuar



while True:
    print("-- MENU --")
    print("1 - Criar novo cliente")
    print("2 - Entrar")
    print("3 - Sair")
    try:
        opc = int(input("Digite uma opção: "))
        system('cls')
    except ValueError:
        print("Digite um número válido!")

    if opc == 1:
        nome = input("Digite seu nome: ")
        email = input("Digite seu email: ") 

        if not validar_email(email):
            print("Email inválido!")
            continue

        cpf = input("Digite seu CPF: ")
        endereco = input("Cadastre seu endereço: ")
        senha = pwinput.pwinput("Digite sua senha: ")
        insert_cliente(nome, email, cpf, endereco, senha)

    elif opc ==2:
        email = input("Digite seu email: ") 
        senha = pwinput.pwinput("Digite sua senha: ")
        admin = validar_admin(email)
        user_auth = login(email, senha)
        if user_auth and admin:
            admin_panel(user_auth) #admin view
        elif user_auth:
            print(f"Bem vindo {user_auth[1]}")
            user_panel(user_auth)
        else:
            print("Usuário ou senha inválidos!")

    elif opc == 3:
        break
    else:
        print("Digite uma opção válida!")

# Inner join para mostrar as tasks do usuário logado (3x)