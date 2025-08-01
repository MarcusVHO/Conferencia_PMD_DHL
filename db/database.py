#Responsavel por estabelecer comunicacao com banco de dados e estruturar o mesmo de maneira automatica
#Criador: Marcus Vinicius Hilário de Oliveira
#Data: 27/07/2025

#------------------ Importacoes Externas ----------------------
import mysql.connector
#------------------ Importacoes Externas ----------------------


#estabelece comunicacao com o banco
def conectar():
    return mysql.connector.connect(
        user="usuario", 
        password="Senha@2025", 
        host="148.230.76.128", 
        database="banco_de_dados"
    )



#------------------------- Tabelas ----------------------------

#cira tabela de usuarios
def criar_tabela_usuarios():
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

#cira tabela de misturas normais
def criar_tabela_misturas_normais():
    conn = conectar()

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS misturas (
        id INT AUTO_INCREMENT PRIMARY KEY,
        op_numero VARCHAR(50) NOT NULL,
        json_mistura_normal JSON NOT NULL,
        qtd_confirmada INT DEFAULT 0,
        status_mist VARCHAR(20) DEFAULT 'pendente',
        total_mist INT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

    )
    """)
    conn.commit()
    cursor.close()
    conn.close()

#cira tabela de fines
def criar_tabela_fines():
    conn = conectar()

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS fines (
        id INT AUTO_INCREMENT PRIMARY KEY,
        op_numero VARCHAR(50) NOT NULL,
        json_fines JSON NOT NULL,
        qtd_confirmada INT DEFAULT 0,
        status_fines VARCHAR(20) DEFAULT 'pendente',
        total_fines INT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
 
    )
    """)

    conn.commit()
    cursor.close()
    conn.close()



#cira tabela de sts
def criar_tabela_sts():
    conn = conectar()

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sts (
        id INT AUTO_INCREMENT PRIMARY KEY,
        op_numero VARCHAR(50) NOT NULL,
        json_sts JSON NOT NULL,
        qtd_confirmada INT DEFAULT 0,
        status_sts VARCHAR(20) DEFAULT 'pendente',
        total_sts INT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
 
    )
    """)

    conn.commit()
    cursor.close()
    conn.close()



#cira tabela de relacao do sts
def criar_tabela_relacao_sts():
    conn = conectar()

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS relacao_sts (
        id INT AUTO_INCREMENT PRIMARY KEY,
        codigo VARCHAR(20) NOT NULL,
        peso_caixa INT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
 
    )
    """)

    conn.commit()
    cursor.close()
    conn.close()


#------------------------- Tabelas ----------------------------


#------------------- Tabelas Relatorios -----------------------

def criar_tabela_relatorio_mistura_normal():
    conn = conectar()

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS relatorio_mistura (
        id INT AUTO_INCREMENT PRIMARY KEY,
        op VARCHAR(20) NOT NULL,
        codigo VARCHAR(60) NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        nome VARCHAR(50) NOT NULL
                   
 
    )
    """)

    conn.commit()
    cursor.close()
    conn.close()




def criar_tabela_relatorio_fiens():
    conn = conectar()

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS relatorio_fines (
        id INT AUTO_INCREMENT PRIMARY KEY,
        op VARCHAR(20) NOT NULL,
        codigo VARCHAR(60) NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        nome VARCHAR(50) NOT NULL
                   
 
    )
    """)

    conn.commit()
    cursor.close()
    conn.close()




def criar_tabela_relatorio_sts():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS relatorio_sts (
        id INT AUTO_INCREMENT PRIMARY KEY,
        op VARCHAR(20) NOT NULL,
        codigo VARCHAR(60) NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        nome VARCHAR(50) NOT NULL
                   
 
    )
    """)

    conn.commit()
    cursor.close()
    conn.close()

#------------------- Tabelas Relatorios -----------------------

criar_tabela_relatorio_mistura_normal()
criar_tabela_relatorio_fiens()
criar_tabela_relatorio_sts()
criar_tabela_usuarios()
criar_tabela_relacao_sts()
criar_tabela_sts()
criar_tabela_fines()
criar_tabela_misturas_normais()