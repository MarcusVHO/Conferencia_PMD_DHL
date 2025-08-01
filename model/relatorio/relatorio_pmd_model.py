#Responsavel por comunicar com banco de dados para o controler
#Criador: Marcus Vinicius Hilário de Oliveira
#Data: 31/07/2025


#------------------ inportações Externas --------------------
#------------------ inportações Externas --------------------


#------------------ inportações internas --------------------
from db.database import conectar
#------------------ inportações internas --------------------

conn = conectar()


def get_cursor():
    global conn
    if not conn.is_connected():
        conn.reconnect()  # Garante reconexão se caiu
    return conn.cursor()


def obter_lista_de_misturas(tipo):

    cursor = get_cursor()

    sql = f"""
    SELECT DISTINCT op
    FROM relatorio_{tipo.lower()}
    LIMIT 60;
    """
    cursor.execute(sql)

    resultado = cursor.fetchall()

    cursor.close()
    conn.close()

    return resultado




def obter_lancamentos(op, tipo):


    cursor = get_cursor()

    sql = f"""
    SELECT codigo, created_at, nome
    FROM relatorio_{tipo.lower()}
    WHERE op = {op}
    LIMIT 60;
    """
    cursor.execute(sql)

    resultado = cursor.fetchall()

    cursor.close()
    conn.close()

    return resultado
