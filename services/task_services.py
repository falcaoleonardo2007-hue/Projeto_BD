from config.db import criar_conexao

def create_taks(user_id, title): #O user_id na minha tabela represenda o ID do cliente (cliente_ID)
    conn = criar_conexao()
    cursor = conn.cursor()
    sql = "INSERT INTO TASKS (title, user_id) VALUES (%s, %s)"
    cursor.execute(sql, [title, user_id])
    conn.commit()
    conn.close()
    print("Task cadastrada!")

def list_tasks(user_id):
    conn = criar_conexao()
    cursor = conn.cursor()
    sql = 'SELECT * FROM TASKS WHERE user_id = %s'
    cursor.execute(sql, [user_id])
    tasks = cursor.fetchall() #Retorna uma lista de tasks
    return tasks

def delete_task(user_id, task_id):
    conn = criar_conexao()
    cursor = conn.cursor()
    sql = 'DELETE FROM tasks WHERE user_id=%s AND id=%s'
    cursor.execute(sql, [user_id, task_id])
    conn.commit()
    print("Task Removida!")

def update_task(user_id, task_id, title):
    conn = criar_conexao()
    cursor = conn.cursor()
    sql = 'UPDATE tasks SET title = %s WHERE user_id = %s AND id = %s'
    cursor.execute(sql, [title, user_id, task_id])
    conn.commit()
    print("Task atualizada")


def cadastrar_jogo(user_id, nome, genero, plataforma):
    conn = criar_conexao()
    cursor = conn.cursor()
    sql = "INSERT INTO jogos (nome, genero, plataforma, user_id) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, [nome, genero, plataforma, user_id])
    conn.commit()
    conn.close()
    print("Jogo cadastrado!")