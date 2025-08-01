#acessa banco de dados para tela de gerencimento
#Criador: Marcus Vinicius Hilário de Oliveira
#Data: 30/07/2025


#------------------ inportações Externas --------------------
#------------------ inportações Externas --------------------


#------------------ inportações internas --------------------
from db.database import conectar
import config.settings as st
#------------------ inportações internas --------------------

conn = conectar()


def get_cursor():
    global conn
    if not conn.is_connected():
        conn.reconnect()  # Garante reconexão se caiu
    return conn.cursor()


#Obtem lista de misturas que serao mostradas na tela
def listar_mistura(type):

    cursor = get_cursor()

    sql = f"""
        SELECT op, qtd_confirmada, status, total
        FROM {type}
        ORDER BY FIELD(status, 'pendente', 'cancelado', 'concluido'), created_at DESC
        LIMIT 30

    """
    cursor.execute(sql)
    lista = cursor.fetchall()

    cursor.close()
    conn.close()

    return lista




#executa funcao de alterar status
def alterar_status(op, type, status):



    cursor = get_cursor()

    sql = f"""
        UPDATE {type} SET status = %s WHERE op = %s
    """
    cursor.execute(sql, (status, op))
    conn.commit()

    if status == "cancelado":
        cursor = get_cursor()

        update_confirm = f"""
        UPDATE {type} SET qtd_confirmada = 0 WHERE op = %s
        """
        cursor.execute(update_confirm, (op,))
        conn.commit()

        
        


    relatorio = f"""
        INSERT INTO relatorio_{type} (op, codigo, nome)    
        VALUES (%s, %s, %s)
    """
    cursor.execute(relatorio, (op, f"ALTERADO: {status}", st.USUARIO_LOGADO["nomeusuario"]))
    conn.commit()

    cursor.close()
    conn.close()


