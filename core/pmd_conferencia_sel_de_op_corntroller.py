#Controlador do frame de selecao de conferencia
#Criador: Marcus Vinicius Hilário de Oliveira
#Data: 27/07/2025


#------------------ inportações Externas --------------------
import customtkinter as ctk
#------------------ inportações Externas --------------------


#------------------ inportações Internas --------------------
import config.colors as cor
import model.pmd_conferencia_sel_de_op_model as model
from view.components.widgets_reutilizaveis import botao_indentificador
#------------------ inportações Internas --------------------


    
    


def criar_botoes(frame, tipo):
    def ao_clicar(op):
            print(f"{tipo} de OP: {op} selecionada.")



    if tipo == "mistura_normal":
        lista_misturas = model.listar_misturas_normais()

        for mistura in lista_misturas:
            botao = botao_indentificador(frame, mistura[0], mistura[1], mistura[2], mistura[3], 0, ao_clicar)
            botao.pack(pady=10)
            print(mistura)




    elif tipo == "fines":
        lista_fines = model.listar_misturas_fines()

        for mistura in lista_fines:
            botao = botao_indentificador(frame, mistura[0], mistura[1], mistura[2], mistura[3], 0, ao_clicar)
            botao.pack(pady=10)
            print(mistura)


    elif tipo == "sts":
        lista_fines = model.listar_misturas_sts()

        for mistura in lista_fines:
            botao = botao_indentificador(frame, mistura[0], mistura[1], mistura[2], mistura[3], 0, ao_clicar)
            botao.pack(pady=10)
            print(mistura)


