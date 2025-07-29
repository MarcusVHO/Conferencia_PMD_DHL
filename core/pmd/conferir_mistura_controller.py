#Responsavel por controlar conferencia de misturas normais
#Criador: Marcus Vinicius Hilário de Oliveira
#Data: 28/07/2025

#------------------ Importacoes Externas ----------------------
import json
#------------------ Importacoes Externas ----------------------



#------------------ Importacoes Internas ----------------------
import model.pmd.conferir_mistura_model as model
#------------------ Importacoes Internas ----------------------


def atualizar_dados(op, cont):

    dados = model.pegar_dados_uteis(op)
    dados = {
        "misturas": json.loads(dados[0]),
        "confirmados": dados[1],
        "status": dados[2],
        "total": dados[3]
    }
    
    print(dados)
    return dados
    


def conferir_mistura(op, mistura_atual, texto_digitado, confirmados):
    if mistura_atual == texto_digitado:
        confirmados += 1
        model.atualizar_dado(op, confirmados)
        return True