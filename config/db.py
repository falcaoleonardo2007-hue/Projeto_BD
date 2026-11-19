import psycopg2

def criar_conexao():
    try:
        conn = psycopg2.connect(
            dbname='loja_de_jogos',
            user='postgres',
            password='16L03r',
            host='127.0.0.1',
            port='5432'
        )
        # print("Conectado com sucesso!")
        return conn
    except Exception as e:
        print(f"Erro de conexão {e}")
        return None

