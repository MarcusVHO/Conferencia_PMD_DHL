#Model da conferencia de misturas
#Criador: Marcus Vinicius Hilário de Oliveira
#Data: 28/07/2025


#------------------ inportações Externas --------------------
#------------------ inportações Externas --------------------


#------------------ inportações Internas --------------------
import config.settings as st
from db.database import conectar
#------------------ inportações Internas --------------------

conn = conectar()


def get_cursor():
    global conn
    if not conn.is_connected():
        conn.reconnect()  # Garante reconexão se caiu
    return conn.cursor()


#Pega os dados que serao usados no controle e view
def pegar_dados_uteis(op, type):
    cursor = get_cursor()

    if type == "mistura_normal":
    
        sql = """
            SELECT json_mistura_normal,qtd_confirmada, status_mist, total_mist
            FROM misturas
            WHERE op_numero = %s

        """
        cursor.execute(sql, (op,))
        resultado = cursor.fetchall()[0]

        return resultado
    

    #Pèga dados dos fines
    elif type == "fines":
    
        sql = """
            SELECT json_fines,qtd_confirmada, status_fines, total_fines
            FROM fines
            WHERE op_numero = %s

        """
        cursor.execute(sql, (op,))
        resultado = cursor.fetchall()[0]

        return resultado
    

    #pega dados dos sts
    elif type == "sts":
    
        sql = """
            SELECT json_sts, qtd_confirmada, status_sts, total_sts
            FROM sts
            WHERE op_numero = %s

        """
        cursor.execute(sql, (op,))
        resultado = cursor.fetchall()[0]

        return resultado
    
    cursor.close()


def atualizar_dado(op, confirmados, type):
    cursor = get_cursor()

    if type == "mistura_normal":
        sql = """
            UPDATE misturas SET qtd_confirmada = %s WHERE op_numero = %s
        """
        valores = (confirmados, op)
        cursor.execute(sql, valores)
        conn.commit()


    elif type == "fines":
        sql = """
            UPDATE fines SET qtd_confirmada = %s WHERE op_numero = %s
        """
        valores = (confirmados, op)
        cursor.execute(sql, valores)
        conn.commit()


    elif type == "sts":
        sql = """
            UPDATE sts SET qtd_confirmada = %s WHERE op_numero = %s
        """
        valores = (confirmados, op)
        cursor.execute(sql, valores)
        conn.commit()

    cursor.close()


#conclui e fecha o model 
def concluir(op, type):
    cursor = get_cursor()

    if type == "mistura_normal":
        sql = """
            UPDATE misturas SET status_mist = %s WHERE op_numero = %s
        """
        valores = ("concluido", op)
        cursor.execute(sql, valores)
        conn.commit()

        relatorio = f"""
            INSERT INTO relatorio_mistura (op, codigo, nome)    
            VALUES (%s, %s, %s)
        """
        cursor.execute(relatorio, (op, f"OP: {op} CONCLUIDA", st.USUARIO_LOGADO["nomeusuario"]))
        conn.commit()


    elif type == "fines":
        sql = """
            UPDATE fines SET status_fines = %s WHERE op_numero = %s
        """
        valores = ("concluido", op)
        cursor.execute(sql, valores)
        conn.commit()

        relatorio = f"""
            INSERT INTO relatorio_fines (op, codigo, nome)    
            VALUES (%s, %s, %s)
        """
        cursor.execute(relatorio, (op, f"OP: {op} CONCLUIDA", st.USUARIO_LOGADO["nomeusuario"]))
        conn.commit()




    elif type == "sts":
        sql = """
            UPDATE sts SET status_sts = %s WHERE op_numero = %s
        """
        valores = ("concluido", op)
        cursor.execute(sql, valores)
        conn.commit()

        relatorio = f"""
            INSERT INTO relatorio_sts (op, codigo, nome)    
            VALUES (%s, %s, %s)
        """
        cursor.execute(relatorio, (op, f"OP: {op} CONCLUIDA", st.USUARIO_LOGADO["nomeusuario"]))
        conn.commit()


    cursor.close()


def inserir_no_relatorio(op, mistura, nome, tipo):
    cursor = get_cursor()


    if tipo =="mistura_normal":
        tipo = "mistura"

        
    sql = f"""
    INSERT INTO relatorio_{tipo} (op, codigo, nome)    
    VALUES (%s, %s, %s)
    """

    cursor.execute(sql, (op, mistura, nome))
    cursor.close()
    conn.commit()
    conn.close()




def inserir_erro_no_relatorio(op, dado, tipo):

    cursor = get_cursor()

    if tipo == "mistura_normal":
        tipo = "mistura"

    sql = f"""
    INSERT INTO relatorio_{tipo} (op, codigo, nome)
    VALUES(%s, %s, %s)
    """
    cursor.execute(sql, (op, dado, st.USUARIO_LOGADO["nomeusuario"]))

    cursor.close()
    conn.commit()
    conn.close()