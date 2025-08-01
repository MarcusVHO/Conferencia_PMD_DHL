#Model do frame de selecao de conferencia
#Criador: Marcus Vinicius Hilário de Oliveira
#Data: 27/07/2025


#------------------ inportações Externas --------------------
#------------------ inportações Externas --------------------


#------------------ inportações Internas --------------------
from db.database import conectar
#------------------ inportações Internas --------------------

conn = conectar()

def get_cursor():
    global conn
    if not conn.is_connected():
        conn.reconnect()  # Garante reconexão se caiu
    return conn.cursor()


def obter_lista(type):
    cursor = get_cursor()

    sql = f"""
    SELECT op, qtd_confirmada, status, total
    FROM {type}
    ORDER BY FIELD(status, 'pendente', 'cancelado', 'concluido'), created_at DESC
    LIMIT 30
    """

    cursor.execute(sql)
    resultado = cursor.fetchall()

    cursor.close()
    conn.close()

    return resultado



def verificar_estado_da_op(op, type):
    cursor = get_cursor()
    
    #verifca estado da misuta normal
    sql = f"""
        SELECT status
        FROM {type}
        WHERE op = {op}

    """
    cursor.execute(sql)
    resultado = cursor.fetchall()


    cursor.close()
    conn.close()

    return resultado

    