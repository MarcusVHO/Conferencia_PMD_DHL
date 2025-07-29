#Model da conferencia de misturas
#Criador: Marcus Vinicius Hilário de Oliveira
#Data: 28/07/2025


#------------------ inportações Externas --------------------
#------------------ inportações Externas --------------------


#------------------ inportações Internas --------------------
from db.database import conectar
#------------------ inportações Internas --------------------
conn = conectar()
cursor = conn.cursor()

def pegar_dados_uteis(op):
    
    sql = """
        SELECT json_mistura_normal,qtd_confirmada, status_mist, total_mist
        FROM misturas
        WHERE op_numero = %s

    """
    cursor.execute(sql, (op,))
    resultado = cursor.fetchall()[0]

    return resultado


def atualizar_dado(op, confirmados):
    
    sql = """
        UPDATE misturas SET qtd_confirmada = %s WHERE op_numero = %s
    """
    valores = (confirmados, op)
    cursor.execute(sql, valores)
    conn.commit()
