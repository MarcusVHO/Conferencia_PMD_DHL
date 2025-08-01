#Responsavel por controlar sistemas do relatorio
#Criador: Marcus Vinicius Hilário de Oliveira
#Data: 31/07/2025


#------------------ inportações Externas --------------------
import customtkinter as ctk
from datetime import datetime, time
#------------------ inportações Externas --------------------


#------------------ inportações internas --------------------
import config.colors as cor
import model.relatorio.relatorio_pmd_model as model
from utils.utilities import *
#------------------ inportações internas --------------------

#objeto botao de op
class botao_op():
    def __init__(self,frame, frame_de_informacoes, op, tipo, ao_clicar=None):


        botao = ctk.CTkButton(
            frame,
            text=op,
            height=40,
            fg_color=cor.DHL_COLORS["warning"],
            text_color=cor.DHL_COLORS["text_dark"],
            font=("Arial", 20, "bold"), 
            border_width=0,
            command=lambda: ao_clicar(op, tipo, frame_de_informacoes, botao) if ao_clicar else None
        )
        botao.pack(fill="x", expand=True, pady=10, padx=10)

#molde das informacoes
class Informacoes():
    def __init__(self, frame, op, codigo, objeto_data, nome):
        self.frame = ctk.CTkFrame(
            frame,
            height=40, 
            fg_color=cor.DHL_COLORS["gray_medium"]
        )
        self.frame.pack(pady=10, padx=10, fill="x", expand=True)



        self.label_codigo = ctk.CTkLabel(
            self.frame,
            text=codigo,
            text_color=cor.DHL_COLORS["text_dark"],
            font=("Arial", 20, "bold")
        )
        self.label_codigo.pack(side="left", padx=10)

        data = objeto_data.strftime("%d/%m/%Y")
        hora = objeto_data.strftime("%H:%M:%S")
        objeto_hora = objeto_data.time()


        primeiro = time(5, 20)
        segundo = time(13, 40)
        terceiro = time(22, 0)


        if primeiro <= objeto_hora < segundo:
            turno = "1ºT"
        elif segundo <= objeto_hora < terceiro:
            turno = "2ºT"
        else:
            turno = "3ºT"



        self.label_data = ctk.CTkLabel(
            self.frame,
            text=data,
            text_color=cor.DHL_COLORS["text_dark"],
            font=("Arial", 20, "bold")
        )
        self.label_data.pack(side="left", padx=10)

        self.label_hora = ctk.CTkLabel(
            self.frame,
            text=hora,
            text_color=cor.DHL_COLORS["text_dark"],
            font=("Arial", 20, "bold")
        )
        self.label_hora.pack(side="left", padx=10)



        self.label_nome = ctk.CTkLabel(
            self.frame,
            text=nome,
            text_color=cor.DHL_COLORS["text_dark"],
            font=("Arial", 20, "bold")
        )
        self.label_nome.pack(side="left", padx=10)


        self.label_turno = ctk.CTkLabel(
            self.frame,
            text=turno,
            text_color=cor.DHL_COLORS["text_dark"],
            font=("Arial", 20, "bold")
        )
        self.label_turno.pack(side="left", padx=10)

        frame.configure(label_text=op)
        frame.configure(label_font=("Arial", 20 , "bold"))
        frame.configure(label_fg_color=cor.DHL_COLORS["gray_dark"])
        frame.configure(label_text_color = cor.DHL_COLORS["text_light"])


ultimo_botao = None

#mostra informacoes de op especifica
def mostrar_informacoes(op, tipo, frame_de_informacoes, botao):

    botao.configure(border_color = cor.DHL_COLORS["secondary"], border_width=3)
    global ultimo_botao
    if ultimo_botao and ultimo_botao.winfo_exists():
        ultimo_botao.configure(border_width = 0)

    ultimo_botao = botao

    informacoes = model.obter_lancamentos(op, tipo)
    limpar_frame(frame_de_informacoes)
    if informacoes:
        for item in informacoes:
            Informacoes(frame_de_informacoes, op, item[0], item[1], item[2])



#lista e coloca no frame 
def listar_misturas(tipo, frame, frame_de_informacoes):
    lista_itens = model.obter_lista_de_misturas(tipo)


    if lista_itens:
        for item in lista_itens:
           botao_op(frame, frame_de_informacoes, item[0], tipo, mostrar_informacoes)