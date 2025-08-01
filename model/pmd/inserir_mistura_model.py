#Responsavel por se comunicar com o banco de dados a orde do controller
#Criador: Marcus Vinicius Hilário de Oliveira
#Data: 27/07/2025

#------------------ inportações Externas --------------------
import json
from db.database import conectar
#------------------ inportações Externas --------------------


#------------------ Misturas e Fines ------------------------

#Isere misturas normais no banco de dados
def inserir_mistura_normal(op, mistura, total, fines, total_fines):
    conn = conectar()
    cursor = conn.cursor()

    check_sql = """
    SELECT COUNT(*) FROM misturas
    WHERE op_numero = %s AND status_mist IN ('pendente', 'concluido', 'cancelado')
    """
    
    cursor.execute(check_sql, (op,))
    existe = cursor.fetchone()[0]

    if existe > 0:
        print(f" Não pode inserir: já existe uma mistura para OP {op} com status cancelado, pendente ou concluído.")
    else:
        # Inserção permitida
        insert_sql_mist = """ 
        INSERT INTO misturas (op_numero, json_mistura_normal, total_mist, status_mist)
        VALUES (%s, %s, %s, 'pendente')
        """
        cursor.execute(insert_sql_mist, (op, json.dumps(mistura), total))

        if fines:
            insert_sql_fines = """ 
            INSERT INTO fines (op_numero, json_fines, total_fines, status_fines)
            VALUES (%s, %s, %s, 'pendente')
            """
            cursor.execute(insert_sql_fines, (op, json.dumps(fines), total_fines))





        conn.commit()
        print(" Dados da mistura normal inseridos com sucesso!")

    cursor.close()
    conn.close()


#lista misturas normais pendentes
def listar_misturas_normais_pendentes():
    conn = conectar()
    cursor = conn.cursor()

    querry = """
    SELECT op_numero, qtd_confirmada, status_mist, total_mist
    FROM misturas
    WHERE status_mist = 'pendente'
    ORDER BY id DESC
    LIMIT 30;
    """

    #executa sql para pegar as ultimas 30 misturas do banco
    cursor.execute(querry)
    ultimas_pendentes = cursor.fetchall()

    


    cursor.close()
    conn.close()
    return ultimas_pendentes

#verifica se mistura tem fines
def verificar_existencia_fines(op):
    conn = conectar()
    cursor = conn.cursor()


    verificar_fines ="""
    SELECT EXISTS(
        SELECT 1 FROM fines
        WHERE op_numero = %s
    )
    """

    cursor.execute(verificar_fines, (op,))

    result = cursor.fetchone()[0]
    cursor.close()
    conn.close()
    return result
    

#------------------ Misturas e Fines ------------------------


#------------------------- STS ------------------------------


def inserir_sts(op_sts, sts, total_sts):
    conn = conectar()
    cursor = conn.cursor()

    check_sql = """
    SELECT COUNT(*) FROM sts
    WHERE op_numero = %s AND status_sts IN ('pendente', 'concluido', 'cancelado')
    """
    
    cursor.execute(check_sql, (op_sts,))
    existe = cursor.fetchone()[0]

    if existe > 0:
        print(f" Não pode inserir: já existe um STS para OP {op_sts} com status cancelado, pendente ou concluído.")
    else:
        # Inserção permitida
        insert_sql_mist = """ 
        INSERT INTO sts (op_numero, json_sts, total_sts, status_sts)
        VALUES (%s, %s, %s, 'pendente')
        """
        cursor.execute(insert_sql_mist, (op_sts, json.dumps(sts), total_sts))


        conn.commit()
        print(" Dados do STS inseridos com sucesso!")

    cursor.close()
    conn.close()


def listar_sts_pendentes():
    conn = conectar()
    cursor = conn.cursor()

    querry = """
    SELECT op_numero, qtd_confirmada, status_sts, total_sts
    FROM sts
    WHERE status_sts = 'pendente'
    ORDER BY id DESC
    LIMIT 30;
    """

    #executa sql para pegar as ultimas 30 sts do banco
    cursor.execute(querry)
    ultimas_pendentes = cursor.fetchall()

    


    cursor.close()
    conn.close()
    return ultimas_pendentes


def obter_peso_caixa(material):
    conn = conectar()
    cursor = conn.cursor()

    sql = """
    SELECT peso_caixa
    FROM relacao_sts
    WHERE codigo = %s
    """
    cursor.execute(sql, (material,))

    peso_caixa = cursor.fetchall()[0][0]
    cursor.close()
    conn.close()
    return peso_caixa
#------------------------- STS ------------------------------
