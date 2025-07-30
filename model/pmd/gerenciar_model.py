#acessa banco de dados para tela de gerencimento
#Criador: Marcus Vinicius Hilário de Oliveira
#Data: 30/07/2025


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


def listar_mistura(tipo):

    cursor = get_cursor()

    if tipo == "NORMAIS":
        sql = """
            SELECT op_numero, qtd_confirmada, status_mist, total_mist
            FROM misturas
            ORDER BY FIELD(status_mist, 'pendente', 'cancelado', 'concluido'), created_at DESC
            LIMIT 30

        """
        cursor.execute(sql)
        lista = cursor.fetchall()
        return lista
    

    elif tipo == "FINES":
        sql = """
            SELECT op_numero, qtd_confirmada, status_fines, total_fines
            FROM fines
            ORDER BY FIELD(status_fines, 'pendente', 'cancelado', 'concluido'), created_at DESC
            LIMIT 30

        """
        cursor.execute(sql)
        lista = cursor.fetchall()
        return lista
    

    elif tipo == "STS":
        sql = """
            SELECT op_numero, qtd_confirmada, status_sts, total_sts
            FROM sts
            ORDER BY FIELD(status_sts, 'pendente', 'cancelado', 'concluido'), created_at DESC
            LIMIT 30

        """
        cursor.execute(sql)
        lista = cursor.fetchall()
        return lista

    cursor.close()


def alterar_status(op, tipo, status):

    cursor = get_cursor()


    if tipo == "NORMAIS":
        sql = """
            UPDATE misturas SET status_mist = %s WHERE op_numero = %s
        """
        valores = (status, op)
        cursor.execute(sql, valores)
        conn.commit()

    elif tipo == "FINES":
        sql = """
            UPDATE fines SET status_fines = %s WHERE op_numero = %s
        """
        valores = (status, op)
        cursor.execute(sql, valores)
        conn.commit()


    elif tipo == "STS":
        sql = """
            UPDATE sts SET status_sts = %s WHERE op_numero = %s
        """
        valores = (status, op)
        cursor.execute(sql, valores)
        conn.commit()
    

    cursor.close()