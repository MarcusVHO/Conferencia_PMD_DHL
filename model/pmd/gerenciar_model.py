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


def listar_mistura(tipo):

    cursor = get_cursor()

    if tipo == "NORMAIS":
        sql = """
            SELECT id, op_numero, qtd_confirmada, status_mist, total_mist
            FROM misturas
            ORDER BY FIELD(status_mist, 'pendente', 'cancelado', 'concluido'), created_at DESC
            LIMIT 30

        """
        cursor.execute(sql)
        lista = cursor.fetchall()
        return lista
    

    elif tipo == "FINES":
        sql = """
            SELECT id, op_numero, qtd_confirmada, status_fines, total_fines
            FROM fines
            ORDER BY FIELD(status_fines, 'pendente', 'cancelado', 'concluido'), created_at DESC
            LIMIT 30

        """
        cursor.execute(sql)
        lista = cursor.fetchall()
        return lista
    

    elif tipo == "STS":
        sql = """
            SELECT id, op_numero, qtd_confirmada, status_sts, total_sts
            FROM sts
            ORDER BY FIELD(status_sts, 'pendente', 'cancelado', 'concluido'), created_at DESC
            LIMIT 30

        """
        cursor.execute(sql)
        lista = cursor.fetchall()
        return lista

    cursor.close()
    conn.close()






def alterar_status(op, tipo, status, id):

    cursor = get_cursor()


    if tipo == "NORMAIS":
        sql = """
            UPDATE misturas SET status_mist = %s WHERE id = %s LIMIT 1
        """
        valores = (status, id)
        cursor.execute(sql, valores)
        conn.commit()

        if status == "cancelado":
            update_confirm = """
            UPDATE misturas SET qtd_confirmada = 0 WHERE id = %s
            """
            cursor.execute(update_confirm, (id,))
            conn.commit()

            

        relatorio = f"""
            INSERT INTO relatorio_mistura (op, codigo, nome)    
            VALUES (%s, %s, %s)
        """
        cursor.execute(relatorio, (op, f"ALTERADO: {status}", st.USUARIO_LOGADO["nomeusuario"]))
        conn.commit()




    elif tipo == "FINES":
        sql = """
            UPDATE fines SET status_fines = %s WHERE id = %s
        """
        valores = (status, id)
        cursor.execute(sql, valores)
        conn.commit()

        if status == "cancelado":
            update_confirm = """
            UPDATE fines SET qtd_confirmada = 0 WHERE id = %s
            """
            cursor.execute(update_confirm, (id,))
            conn.commit()

        relatorio = f"""
            INSERT INTO relatorio_fines (op, codigo, nome)    
            VALUES (%s, %s, %s)
        """

        cursor.execute(relatorio, (op, f"ALTERADO: {status}", st.USUARIO_LOGADO["nomeusuario"]))
        conn.commit()



    elif tipo == "STS":
        sql = """
            UPDATE sts SET status_sts = %s WHERE id = %s
        """
        valores = (status, id)
        cursor.execute(sql, valores)
        conn.commit()


        if status == "cancelado":
            update_confirm = """
            UPDATE sts SET qtd_confirmada = 0 WHERE id = %s
            """
            cursor.execute(update_confirm, (id,))
            conn.commit()

        relatorio = f"""
            INSERT INTO relatorio_sts (op, codigo, nome)    
            VALUES (%s, %s, %s)
        """

        cursor.execute(relatorio, (op, f"ALTERADO: {status}", st.USUARIO_LOGADO["nomeusuario"]))
        conn.commit()

    cursor.close()
    conn.close()