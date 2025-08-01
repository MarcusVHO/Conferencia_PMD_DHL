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


    sql = f"""
        SELECT misturas, qtd_confirmada, status, total
        FROM {type.lower()}
        WHERE op = %s

    """
    cursor.execute(sql, (op,))
    resultado = cursor.fetchall()[0]
    cursor.close()
    conn.close()
    return resultado
    

#Atuliza a quantidade confirmado do item que esta sendo conferido a cada conferencia
def atualizar_dado(op, confirmados, type):
    cursor = get_cursor()

   
    sql = f"""
        UPDATE {type} SET qtd_confirmada = %s WHERE op = %s
    """
    cursor.execute(sql, (confirmados, op))
    conn.commit()
    cursor.close()
    conn.close()




#conclui o item conferido e insere no relatorio
def concluir(op, type):
    cursor = get_cursor()

    sql = f"""
        UPDATE {type} SET status = %s WHERE op = %s
    """
    valores = ("concluido", op)
    cursor.execute(sql, valores)
    conn.commit()

    relatorio = f"""
        INSERT INTO relatorio_{type} (op, codigo, nome)    
        VALUES (%s, %s, %s)
    """
    cursor.execute(relatorio, (op, f"OP: {op} CONCLUIDA", st.USUARIO_LOGADO["nomeusuario"]))
    conn.commit()
    cursor.close()
    conn.close()




#insere cada dado conferido no relatorio
def inserir_no_relatorio(op, mistura, nome, tipo):
    cursor = get_cursor()


        
    sql = f"""
    INSERT INTO relatorio_{tipo} (op, codigo, nome)    
    VALUES (%s, %s, %s)
    """

    cursor.execute(sql, (op, mistura, nome))
    conn.commit()
    cursor.close()
    conn.close()



#insere o erro no relatorio
def inserir_erro_no_relatorio(op, dado, tipo):

    cursor = get_cursor()

    sql = f"""
    INSERT INTO relatorio_{tipo} (op, codigo, nome)
    VALUES(%s, %s, %s)
    """
    cursor.execute(sql, (op, dado, st.USUARIO_LOGADO["nomeusuario"]))

    conn.commit()
    cursor.close()
    conn.close()
