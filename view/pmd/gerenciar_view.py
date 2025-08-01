#Tela reponsavel pelo gerenciamento administrativo das misturas
#Criador: Marcus Vinicius Hilário de Oliveira
#Data: 30/07/2025


#------------------ inportações Externas --------------------
import customtkinter as ctk
from PIL import Image
#------------------ inportações Externas --------------------


#------------------ inportações internas --------------------
import config.colors as cor
import core.pmd.gerenciar_controller as core
from utils.utilities import *
from view.components.screen_components import *
#------------------ inportações internas --------------------


#classe principal
class Gerenciar(ctk.CTkFrame):
    def __init__(self, master, navigate_to_home_pmd):

        #inicializaca primaria
        super().__init__(master)
        self.navigate_to_home_pmd = navigate_to_home_pmd

        #inicializacao de variaveis
        self.tipo = None


        #inicializacao do frame principal
        self.frame = ctk.CTkFrame(self, fg_color=cor.DHL_COLORS["primary"])
        self.frame.pack(fill="both", expand=True)


        #inicializacao de elementos cabecalho e rodape
        Cabecalho(self.frame, "GERENCIAR MISTURAS")
        rodape = Rodape(self.frame, True, self.Voltar)
        rodape.entry_OPT.destroy()
        rodape.label_OPT.destroy()

        #--------------- contrucao principal ------------------
        
        #conteiner
        self.frame_conteiner = ctk.CTkFrame(
            self.frame,
            width=1200
        )
        self.frame_conteiner.pack(fill="y", expand=True, pady=10)
        self.frame_conteiner.pack_propagate(False)


        #------------ cabecalho ------------

        #frame
        self.frame_header = ctk.CTkFrame(
            self.frame_conteiner,
            height=80,
            fg_color=cor.DHL_COLORS["gray_dark"]
        )
        self.frame_header.pack(side="top", fill="x", anchor="n")
        self.frame_header.pack_propagate(False)

        #titulo
        label_titulo_header = ctk.CTkLabel(
            self.frame_header,
            text="Gerenciar Misturas",
            text_color=cor.DHL_COLORS["text_light"],
            font=("Arial", 30, "bold")
        )
        label_titulo_header.pack(side="left", anchor="center", padx=20)

        #botao
        self.botao_seletor = ctk.CTkSegmentedButton(
            self.frame_header,
            height=60,
            values=["NORMAIS", "FINES", "STS"],
            text_color=cor.DHL_COLORS["text_light"],
            fg_color=cor.DHL_COLORS["gray_dark"],
            command=self.seletor_de_tipo
        )
        self.botao_seletor.pack(anchor="center", side="right", padx=20, pady=10)
        
        #------------ cabecalho ------------

        #----------- Frame Central -----------

        self.frame_central = ctk.CTkScrollableFrame(
            self.frame_conteiner,
            
        )
        self.frame_central.pack(fill="both", expand=True, padx=20, pady=20)

        #----------- Frame Central -----------





        #--------------- contrucao principal ------------------


    def seletor_de_tipo(self, values):

        if values == "NORMAIS":
            values = "mistura"

        values = values.lower()
        limpar_frame(self.frame_central)
        core.mostrar_mistura(values, self.frame_central, self.atualizar_tela)
        print(values)
        self.tipo = values

    def Voltar(self, event=None):
        self.navigate_to_home_pmd()


    def atualizar_tela(self, event=None):
        limpar_frame(self.frame_central)
        core.mostrar_mistura(self.tipo, self.frame_central, self.atualizar_tela)

       