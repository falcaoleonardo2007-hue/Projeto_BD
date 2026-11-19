from services.task_services import create_taks, list_tasks, delete_task, update_task
from os import system #system cls
from msvcrt import getch #getch() - Pressionar tecla para continuar


# ('Leonardo Falcão', 'admin1@gmail.com', '11100011100','Rual Comendador', 'admin123', True) - Tupla com os dados cadastrados do admin
def admin_panel(user_auth):
    while True:
        print(f"Bem vindo {user_auth[1]}")
        print("1 - Cadastras task")
        print("2 - Listar task")
        print("3 - Remover task")
        print("4 - Atualizar task")
        print("5 - Deslogar")

        opc = int(input("Digite uma opção: "))

        if opc == 1:
            title = input("Digite o título da tarefa: ")
            create_taks(user_auth[0], title)
        elif opc == 2:
            tasks = list_tasks(user_auth[0])
            for task in tasks:
                print(f"Suas tasks: {task[0]} - {task[1]}")
                print("Pressione uma tecla para continuar...")
                getch()
        elif opc == 3:
            id_task = int(input("Digite o id da task para remover: "))
            delete_task(user_auth[0], id_task)
        elif opc == 4:
            id_task = int(input("Digite o id da task para atualizar: "))
            new_title = input("Digite o novo título da task: ")
            update_task(user_auth[0], id_task, new_title)
        elif opc == 5:
            system('cls')
            break
        else:
            print("Digite uma opção válida!")