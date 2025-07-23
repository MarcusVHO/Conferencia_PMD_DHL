import mysql.connector

def conectar():
    return mysql.connector.connect(
        user="root", 
        password="21012006", 
        host="localhost", 
        database="usuarios"
    )


def criar_tabela():
    conn = conectar()

    cursor = conn.cursor()

    cursor.execute(""" CREATE TABLE IF NOT EXISTS usuarios (id INT AUTO_INCREMENT PRIMARY KEY, nome VARCHAR(100) NOT NULL, email VARCHAR(100))""")
    conn.commit()
    conn.close()



def inserir_usuarios(nome, email):
    conn = conectar()
    cursor = conn.cursor()

    sql = "INSERT INTO usuarios (nome, email) VALUES (%s, %s)"
    valores = (nome, email)

    cursor.execute(sql, valores)
    conn.commit()
    conn.close()


def listar_usuarios():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM usuarios")
    for usuario in cursor.fetchall():
        print(usuario)

    conn.close()


criar_tabela()
listar_usuarios()