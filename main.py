from services.user_services import insert_cliente, login, validar_admin
from view.admin_view import admin_panel
from view.user_view import user_panel
import pwinput
from validacoes.regex import validar_email, validar_senha
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
        continue

    if opc == 1:
        nome = input("Digite seu nome: ")
        while True:
            email = input("Digite seu email: ") 

            if not validar_email(email):
                print("Email inválido!")
                continue
            else: 
                break

        cpf = input("Digite seu CPF: ")
        endereco = input("Cadastre seu endereço: ")

        while True:
            senha = pwinput.pwinput("Digite sua senha: ")

            if not validar_senha(senha):
                print("\nSenha inválida! A senha precisa conter:")
                print("- No mínimo 8 caracteres.")
                print("- Pelo menos uma letra minúscula.")
                print("- Pelo menos uma letra maiúscula.")
                print("- Pelo menos um número.")
                print("- Pelo menos um caractere especial (!@#$%&*).\n")
                continue
            else:
                break

        insert_cliente(nome, email, cpf, endereco, senha)

    elif opc ==2:
        
        email = input("Digite seu email: ") 
        senha = pwinput.pwinput("Digite sua senha: ")
        admin = validar_admin(email)
        user_auth = login(email, senha)
        
        if user_auth and admin:
            system('cls')
            admin_panel(user_auth) #admin view
        elif user_auth:
            system('cls')
            user_panel(user_auth)
        else:
            print("Usuário ou senha inválidos!")

    elif opc == 3:
        break
    else:
        print("Digite uma opção válida!")
