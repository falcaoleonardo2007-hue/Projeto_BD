from config.db import criar_conexao
from config.crypt import checar_password, criptografar


def insert_cliente(nome: str, email: str, cpf: str, endereco: str, senha:str):
    try:
        con = criar_conexao()
        cursor = con.cursor()
        senha = criptografar(senha)
        sql = "INSERT INTO Usuarios(nome, email, cpf, endereco, senha) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(sql, (nome, email, cpf, endereco, senha))
        con.commit()
        print("Usuarios cadastrado com sucesso!")


    except Exception as e:
        print(e)
    finally:

        cursor.close()
        con.close()

def login(email: str, senha:str):
    try:
        con = criar_conexao()
        cursor = con.cursor()
        sql = "SELECT * FROM Usuarios WHERE email=%s"
        cursor.execute(sql, (email,))
        user = cursor.fetchone()
        if user and checar_password(senha, bytes(user[4])):
            return user

        return None            
    except Exception as e:
        print(e)

def validar_admin(email: str):
    try:
        con = criar_conexao()
        cursor = con.cursor()
        sql = "SELECT admin FROM Usuarios WHERE email=%s"
        cursor.execute(sql, (email,))
        user = cursor.fetchone()
        if user:
            return bool(user[0]) 
        return False
    except Exception as e:
        print(e)
        return False
    finally:
        if con:
            cursor.close()
            con.close() 


def insert_admin(nome: str, email: str, cpf: str, endereco: str, senha:str):
    try:
        con = criar_conexao()
        cursor = con.cursor()
        senha = criptografar(senha)
        sql = "INSERT INTO Usuarios(nome, email, cpf, endereco, senha, admin) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(sql, (nome, email, cpf, endereco, senha, True))
        con.commit()
        print("Admin cadastrado com sucesso!")