from config.db import criar_conexao

def criar_pedido(user_id):
    conn = criar_conexao()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT carrinho_ID FROM Carrinho WHERE usuario_ID = %s", (user_id,))
        resultado = cursor.fetchone()
        if resultado is None:
            print("Carrinho vazio!")
            return None
        carrinho_ID = resultado[0]

        sql = """
            SELECT COALESCE(SUM(Jogos.valor), 0), COUNT(*)
            FROM Jogo_Carrinho
            INNER JOIN Jogos ON Jogos.jogos_ID = Jogo_Carrinho.jogos_ID
            WHERE Jogo_Carrinho.carrinho_ID = %s
        """
        cursor.execute(sql, (carrinho_ID,))
        total, qtd = cursor.fetchone()
        if qtd == 0:
            print("Carrinho vazio!")
            return None

        cursor.execute("INSERT INTO Pedido (usuario_ID) VALUES (%s) RETURNING pedido_ID", (user_id,))
        pedido_ID = cursor.fetchone()[0]

        sql = """
            INSERT INTO Jogo_Pedido (pedido_ID, jogos_ID)
            SELECT %s, jogos_ID FROM Jogo_Carrinho WHERE carrinho_ID = %s
        """
        cursor.execute(sql, (pedido_ID, carrinho_ID))
        conn.commit()
        return pedido_ID, total

    except Exception as erro:
        conn.rollback()
        print(f"Erro ao criar pedido: {erro}")
        return None

    finally:
        cursor.close()
        conn.close()


def pagar_pedido(user_id, pedido_id):
    conn = criar_conexao()
    cursor = conn.cursor()
    try:
        sql = """
            SELECT COALESCE(SUM(Jogos.valor), 0)
            FROM Pedido
            INNER JOIN Jogo_Pedido ON Jogo_Pedido.pedido_ID = Pedido.pedido_ID
            INNER JOIN Jogos ON Jogos.jogos_ID = Jogo_Pedido.jogos_ID
            WHERE Pedido.pedido_ID = %s AND Pedido.usuario_ID = %s
        """
        cursor.execute(sql, (pedido_id, user_id))
        total = cursor.fetchone()[0]
        if total == 0:
            print("Pedido não encontrado!")
            return False

        cursor.execute("INSERT INTO Pagamento (pedido_ID, valor) VALUES (%s, %s)", (pedido_id, total))

        cursor.execute(
            "DELETE FROM Jogo_Carrinho WHERE carrinho_ID IN "
            "(SELECT carrinho_ID FROM Carrinho WHERE usuario_ID = %s)", (user_id,))
        cursor.execute("UPDATE Carrinho SET quantidade_jogos = 0 WHERE usuario_ID = %s", (user_id,))

        conn.commit()
        return True

    except Exception as erro:
        conn.rollback()
        print(f"Erro ao pagar pedido: {erro}")
        return False

    finally:
        cursor.close()
        conn.close()


def cancelar_pedido(pedido_id):
    conn = criar_conexao()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM Jogo_Pedido WHERE pedido_ID = %s", (pedido_id,))
        cursor.execute("DELETE FROM Pedido WHERE pedido_ID = %s", (pedido_id,))
        conn.commit()
    except Exception as erro:
        conn.rollback()
        print(f"Erro ao cancelar pedido: {erro}")
    finally:
        cursor.close()
        conn.close()