#Respnsavel por realizar busca no banco de dados da tela de login
#Criador: Marcus Vinicius Hilário de Oliveira
#Data: 25/07/2025

#------------------ inportações --------------------
from db.database import conectar
#------------------ inportações --------------------

def buscar_usuarios():
    conn = conectar()
    cursor = conn.cursor(dictionary=True)  # Retorno como dicionário

    # Busca todos os usuários
    sql = "SELECT idusuario, nomeusuario, permissao, senha FROM usuarios"
    cursor.execute(sql)
    resultado = cursor.fetchall()  # pega todos os registros

    cursor.close()
    conn.close()

    return resultado  # Lista de dicionários
