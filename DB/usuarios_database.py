import mysql.connector

def conectar():
    return mysql.connector.connect(
        user="usuario", 
        password="Senha@2025", 
        host="148.230.76.128", 
        database="banco_de_dados"
    )


def criar_tabela():
    conn = conectar()

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            idusuario VARCHAR(50) NOT NULL,
            nomeusuario VARCHAR(50) NOT NULL,
            senha VARCHAR(255) NOT NULL,
            permissao VARCHAR(20) NOT NULL,
            PRIMARY KEY (idusuario)
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()



def inserir_usuarios(idusuario, nomeusuario, senha, permissao):
    conn = conectar()
    cursor = conn.cursor()

    sql = "INSERT INTO usuarios (idusuario, nomeusuario, senha, permissao) VALUES (%s, %s, %s, %s)"
    valores = (idusuario, nomeusuario, senha, permissao)

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

def logar(idusuario, senha_digitada):
    conn = conectar()
    cursor = conn.cursor(dictionary=True)  # para retornar resultado como dicionário

    # Busca senha e outros dados do usuário
    sql = "SELECT idusuario, nomeusuario, permissao, senha FROM usuarios WHERE idusuario = %s"
    cursor.execute(sql, (idusuario,))
    resultado = cursor.fetchone()

    cursor.close()
    conn.close()

    if resultado is None:
        return False  # Usuário não existe

    senha_armazenada = resultado.pop('senha')  # remove senha do dicionário e pega o valor

    if senha_armazenada == senha_digitada:
        return resultado  # retorna dicionário com os dados do usuário, sem senha
    else:
        return False  # senha errada

    
criar_tabela()