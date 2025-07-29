#Model do frame de selecao de conferencia
#Criador: Marcus Vinicius Hilário de Oliveira
#Data: 27/07/2025


#------------------ inportações Externas --------------------
#------------------ inportações Externas --------------------


#------------------ inportações Internas --------------------
from db.database import conectar
#------------------ inportações Internas --------------------


def listar_misturas_normais():
    conn = conectar()
    cursor = conn.cursor()

    sql = """
    SELECT op_numero, qtd_confirmada, status_mist, total_mist
    FROM misturas
    ORDER BY FIELD(status_mist, 'pendente', 'cancelado', 'concluido'), created_at DESC
    LIMIT 30
    """

    cursor.execute(sql)
    resultado = cursor.fetchall()

    cursor.close()
    conn.close()

    return resultado



def listar_misturas_fines():
    conn = conectar()
    cursor = conn.cursor()

    sql = """
    SELECT op_numero, qtd_confirmada, status_fines, total_fines
    FROM fines
    ORDER BY FIELD(status_fines, 'pendente', 'cancelado', 'concluido'), created_at DESC
    LIMIT 30
    """

    cursor.execute(sql)
    resultado = cursor.fetchall()

    cursor.close()
    conn.close()

    return resultado


def listar_misturas_sts():
    conn = conectar()
    cursor = conn.cursor()

    sql = """
    SELECT op_numero, qtd_confirmada, status_sts, total_sts
    FROM sts
    ORDER BY FIELD(status_sts, 'pendente', 'cancelado', 'concluido'), created_at DESC
    LIMIT 30
    """

    cursor.execute(sql)
    resultado = cursor.fetchall()

    cursor.close()
    conn.close()

    return resultado


def verificar_estado_da_op(op, tipo):
    conn = conectar()
    cursor = conn.cursor()
    
    #verifca estado da misuta normal
    if tipo == "mistura_normal":
        sql = """
            SELECT status_mist
            FROM misturas
            WHERE op_numero = %s

        """
        cursor.execute(sql, (op,))
        resultado = cursor.fetchall()[0]

    #verifica estado dos fines
    if tipo == "fines":
        sql = """
            SELECT status_fines
            FROM fines
            WHERE op_numero = %s

        """
        cursor.execute(sql, (op,))
        resultado = cursor.fetchall()[0]


    #verifica estado dos sts
    if tipo == "sts":
        sql = """
            SELECT status_sts
            FROM sts
            WHERE op_numero = %s

        """
        cursor.execute(sql, (op,))
        resultado = cursor.fetchall()[0]


    cursor.close()
    conn.close()

    return resultado

    