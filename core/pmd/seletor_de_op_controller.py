#Controlador do frame de selecao de conferencia
#Criador: Marcus Vinicius Hilário de Oliveira
#Data: 27/07/2025


#------------------ inportações Externas --------------------
import customtkinter as ctk
import winsound
#------------------ inportações Externas --------------------


#------------------ inportações Internas --------------------
import config.colors as cor
import model.pmd.seletro_de_op_model as model
from view.pmd.conferir_mistura_view import Conferir_Mistura
from view.components.widgets_reutilizaveis import botao_indentificador
#------------------ inportações Internas --------------------


    


def criar_botoes(frame, tipo, conferir_mistura):
    pendente = 0
    cancelado = 0
    concluido = 0

    #executa acao ao clicar no botao
    def ao_clicar(op, status):
            
            print(f"{tipo} de OP: {op} selecionada.")

            print(f"Status da OP: {op} é ",status)

            if status == "pendente":
                conferir_mistura(op, tipo)
            else:
                print("Erro")
                winsound.MessageBeep(winsound.MB_ICONHAND)



    lista_misturas = model.obter_lista(tipo)

    for mistura in lista_misturas:
        botao = botao_indentificador(frame, mistura[0], mistura[1], mistura[2], mistura[3], 0, ao_clicar)


        if mistura[2] == "pendente":
            pendente +=1
        if mistura[2] == "concluido":
            concluido+=1
        if mistura[2] == "cancelado":
            cancelado +=1


        botao.pack(pady=10)
        print(mistura)

    return pendente, cancelado, concluido




def entrada_manual(op, type, conferir_mistura):
    if op != "":
        print(f"{type} de OP: {op} selecionada.")
        status = model.verificar_estado_da_op(op, type)
        status = [item[0] for item in status]
        print(f"Status da OP: {op} é ",status)

        if "pendente" in status:
            conferir_mistura(op, type)
        else:
            print("Erro")
            winsound.MessageBeep(winsound.MB_ICONHAND)

