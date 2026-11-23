from config.db import criar_conexao

# - CRUD para a tabela Desenvolvedoras - 
def cadastrar_desenvolvedora(nome, CEP, CNPJ):
    conn = criar_conexao()
    cursor = conn.cursor()
    sql = "INSERT INTO Desenvolvedoras (nome, CEP, CNPJ) VALUES (%s, %s, %s)"
    cursor.execute(sql, [nome, CEP, CNPJ])
    conn.commit()
    conn.close()
    print("Desenvolvedora cadastrada!")

def listar_desenvolvedoras():
    conn = criar_conexao()
    cursor = conn.cursor()
    sql = 'SELECT * FROM Desenvolvedoras'
    cursor.execute(sql)
    desenvolvedoras = cursor.fetchall() #Retorna uma lista de desenvolvedoras
    cursor.close()
    conn.close()
    return desenvolvedoras

def deletar_desenvolvedora(desenvolvedora_id):
    conn = criar_conexao()
    cursor = conn.cursor()
    try:
        sql = 'DELETE FROM Desenvolvedoras WHERE dev_id= %s'
        cursor.execute(sql, (desenvolvedora_id,))
        if cursor.rowcount == 0:
            print("Desenvolvedora não encontrada!")
            return
        conn.commit()
        print("Desenvolvedora removida!")
    except Exception as erro:
        conn.rollback()
        print(f"Erro ao remover desenvolvedora: {erro}")
    finally:
        cursor.close()
        conn.close()

def atualizar_desenvolvedora(desenvolvedora_id, nome, CEP, CNPJ):
    conn = criar_conexao()
    cursor = conn.cursor()
    try:
        sql = 'UPDATE Desenvolvedoras SET nome = %s, CEP = %s, CNPJ = %s WHERE dev_id= %s'
        cursor.execute(sql, (nome, CEP, CNPJ, desenvolvedora_id))
        if cursor.rowcount == 0:
            print("Desenvolvedora não encontrada!")
            return
        conn.commit()
        print("Desenvolvedora atualizada!")
    except Exception as erro:
        conn.rollback()
        print(f"Erro ao atualizar desenvolvedora: {erro}")
    finally:
        cursor.close()
        conn.close()

def count_games_por_dev():
    conn = criar_conexao()
    cursor = conn.cursor()
    try:
        sql = """
            SELECT Desenvolvedoras.nome, COUNT(Jogos.jogos_ID)
            FROM Desenvolvedoras
            INNER JOIN Jogos ON Jogos.dev_id = Desenvolvedoras.dev_ID
            GROUP BY Desenvolvedoras.nome
            ORDER BY COUNT(Jogos.jogos_ID) DESC
        """
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as erro:
        print(f"Erro ao gerar relatório: {erro}")
        return []
    finally:
        cursor.close()
        conn.close()

# - CRUD para a tabela Jogos - 
def create_games(nome, valor, data_lancamento, genero, tamanho, dev_id): #O user_id na minha tabela represenda o ID do admin (cliente_ID)
    conn = criar_conexao()
    cursor = conn.cursor()
    sql = "INSERT INTO Jogos (nome, valor, data_lancamento, genero, tamanho, dev_id) VALUES (%s, %s, %s, %s, %s, %s)"
    cursor.execute(sql, [nome, valor, data_lancamento, genero, tamanho, dev_id])
    conn.commit()
    conn.close()
    print("Jogo cadastrado!")

def list_games():
    conn = criar_conexao()
    cursor = conn.cursor()
    sql = 'SELECT * FROM Jogos'
    cursor.execute(sql)
    jogos = cursor.fetchall()
    return jogos

def delete_game(game_ID):
    conn = criar_conexao()
    cursor = conn.cursor()
    sql = 'DELETE FROM Jogos WHERE jogos_id=%s'
    cursor.execute(sql, [game_ID])
    conn.commit()
    print("Jogo Removido!")

def update_game(game_ID, nome, valor, data_lacamento, genero, tamanho, dev_id):
    conn = criar_conexao()
    cursor = conn.cursor()
    sql = 'UPDATE Jogos SET nome = %s, valor = %s, data_lacamento = %s, genero = %s, tamanho = %s, dev_id = %s WHERE jogos_id = %s'
    cursor.execute(sql, [nome, valor, data_lacamento, genero, tamanho, dev_id, game_ID])
    conn.commit()
    print("Jogo atualizado!")

# - Adicionar jogo no carrinho do usuário - 
def add_game_to_cart(user_id, game_name):
    conn = criar_conexao()
    cursor = conn.cursor()

    try:
        sql = "SELECT jogos_ID FROM Jogos WHERE nome ILIKE %s"
        cursor.execute(sql, (game_name,))
        resultado = cursor.fetchone()
        if resultado is None:
            print("Jogo não encontrado!")
            return

        game_ID = resultado[0]

        sql = "SELECT carrinho_ID FROM Carrinho WHERE usuario_ID = %s"
        cursor.execute(sql, (user_id,))
        resultado = cursor.fetchone()

        if resultado is None:
            sql = "INSERT INTO Carrinho (usuario_ID, quantidade_jogos) VALUES (%s, 0) RETURNING carrinho_ID"
            cursor.execute(sql, (user_id,))
            resultado = cursor.fetchone()

        carrinho_ID = resultado[0]

        sql = "INSERT INTO Jogo_Carrinho (carrinho_ID, jogos_ID) VALUES (%s, %s)"
        cursor.execute(sql, (carrinho_ID, game_ID))
        sql = "UPDATE Carrinho SET quantidade_jogos = quantidade_jogos + 1 WHERE carrinho_ID = %s"
        cursor.execute(sql, (carrinho_ID,))
        conn.commit()
        print("Jogo adicionado ao carrinho!")

    except Exception as erro:
        conn.rollback()
        print(f"Erro ao adicionar jogo: {erro}")

    finally:
        cursor.close()
        conn.close()

def list_cart_games(user_id):
    conn = criar_conexao()
    cursor = conn.cursor()

    try:
        sql = """
            SELECT Jogos.nome, Jogos.valor
            FROM Carrinho
            INNER JOIN Jogo_Carrinho ON Jogo_Carrinho.carrinho_ID = Carrinho.carrinho_ID
            INNER JOIN Jogos ON Jogos.jogos_ID = Jogo_Carrinho.jogos_ID
            WHERE Carrinho.usuario_ID = %s
        """
        cursor.execute(sql, (user_id,))
        return cursor.fetchall()

    except Exception as erro:
        print(f"Erro ao listar jogos do carrinho: {erro}")
        return []

    finally:
        cursor.close()
        conn.close()

def remove_game_from_cart(user_id, game_name):
    conn = criar_conexao()
    cursor = conn.cursor()

    try:
        sql = "SELECT jogos_ID FROM Jogos WHERE nome ILIKE %s"
        cursor.execute(sql, (game_name,))
        resultado = cursor.fetchone()
        if resultado is None:
            print("Jogo não encontrado!")
            return

        game_ID = resultado[0]
        sql = "SELECT carrinho_ID FROM Carrinho WHERE usuario_ID = %s"
        cursor.execute(sql, (user_id,))
        resultado = cursor.fetchone()

        if resultado is None:
            print("Carrinho vazio!")
            return

        carrinho_ID = resultado[0]
        sql = "DELETE FROM Jogo_Carrinho WHERE carrinho_ID = %s AND jogos_ID = %s"
        cursor.execute(sql, (carrinho_ID, game_ID))
        sql = "UPDATE Carrinho SET quantidade_jogos = quantidade_jogos - 1 WHERE carrinho_ID = %s"
        cursor.execute(sql, (carrinho_ID,))
        conn.commit()
        print("Jogo removido do carrinho!")

    except Exception as erro:
        conn.rollback()
        print(f"Erro ao remover jogo: {erro}")

    finally:
        cursor.close()
        conn.close()

def gerenciar_usuarios():
    conn = criar_conexao()
    cursor = conn.cursor()
    try:
        while True:
            print("1 - Listar usuários")
            print("2 - Remover usuário")
            print("3 - Atualizar usuário")
            print("4 - Voltar ao menu do admin")

            opc = int(input("Digite uma opção: "))

            if opc == 1:
                sql = "SELECT * FROM Usuarios"
                cursor.execute(sql)
                usuarios = cursor.fetchall()
                for usuario in usuarios:
                    print(f"ID: {usuario[0]}, Nome: {usuario[1]}, Email: {usuario[2]}, CPF: {usuario[3]}, Endereço: {usuario[5]}")
            elif opc == 2:
                user_id = int(input("Digite o ID do usuário para remover: "))
                sql = "DELETE FROM Usuarios WHERE usuario_ID = %s"
                cursor.execute(sql, (user_id,))
                if cursor.rowcount == 0:
                    print("Usuário não encontrado!")
                else:
                    conn.commit()
                    print("Usuário removido!")
            elif opc == 3:
                user_id = int(input("Digite o ID do usuário que quer atualizar: "))
                nome = input("Digite o novo nome do usuário: ")
                email = input("Digite o novo email do usuário: ")
                cpf = input("Digite o novo CPF do usuário: ")
                endereco = input("Digite o novo endereço do usuário: ")
                admin = input("O usuário é admin? (s/n): ").lower() == 's'
                sql = "UPDATE Usuarios SET nome=%s, email=%s, cpf=%s, endereco=%s, admin=%s WHERE usuario_ID = %s"
                cursor.execute(sql, (nome, email, cpf, endereco, admin, user_id))
                if cursor.rowcount == 0:
                    print("Usuário não encontrado!")
                else:
                    conn.commit()
                    print("Usuário atualizado!")
            elif opc == 4:
                break
            else:
                print("Opção inválida!")

    except Exception as e:
        print(f"Erro ao gerenciar usuários: {e}")

    finally:
        cursor.close()
        conn.close()

def list_all_carts():
    conn = criar_conexao()
    cursor = conn.cursor()
    try:
        sql = """
            SELECT Usuarios.nome, Jogos.nome, Jogos.valor
            FROM Usuarios
            INNER JOIN Carrinho ON Carrinho.usuario_ID = Usuarios.usuario_ID
            INNER JOIN Jogo_Carrinho ON Jogo_Carrinho.carrinho_ID = Carrinho.carrinho_ID
            INNER JOIN Jogos ON Jogos.jogos_ID = Jogo_Carrinho.jogos_ID
            ORDER BY Usuarios.nome
        """
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as erro:
        print(f"Erro ao listar carrinhos: {erro}")
        return []
    finally:
        cursor.close()
        conn.close()
