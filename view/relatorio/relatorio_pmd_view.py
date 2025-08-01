#Responsavel por mostrar relatorio do pmd
#Criador: Marcus Vinicius Hilário de Oliveira
#Data: 31/07/2025


#------------------ inportações Externas --------------------
import customtkinter as ctk
#------------------ inportações Externas --------------------


#------------------ inportações internas --------------------
import config.colors as cor
import config.settings as st
from utils.utilities import *
import core.relatorio.relatorio_pmd_controller as core
from view.components.screen_components import *
#------------------ inportações internas --------------------



#classe principal
class Report_PMD(ctk.CTkFrame):
    def __init__(self, master, navigate_to_report):

        #inicializacao primaria
        super().__init__(master)
        self.navigate_to_report = navigate_to_report

        #inicializacao de variaveis


        #frame principal
        self.frame = ctk.CTkFrame(
            self, 
            fg_color=cor.DHL_COLORS["primary"]
        )
        self.frame.pack(fill="both", expand=True)

        #inicializacao de itens da tela
        Cabecalho(self.frame, "RELATORIO PMD")
        Rodape(self.frame, True, self.navigate_to_report)



        #------------------ Construcao Primaria -----------------------

        #frame conteiner
        self.frame_conteiner = ctk.CTkFrame(
            self.frame,
            width=2000
        )
        self.frame_conteiner.pack(fill="y", expand=True, padx=20, pady=20)
        self.frame_conteiner.pack_propagate()

        # ------------------ header ------------------------

        #frame do titulo
        self.frame_titulo = ctk.CTkFrame(
            self.frame_conteiner,
            height=80,
            fg_color=cor.DHL_COLORS["gray_dark"]
        )
        self.frame_titulo.pack(side="top", fill="x")
        self.frame_titulo.pack_propagate(False)

        #titulo do frame
        label_titulo_frame = ctk.CTkLabel(
            self.frame_titulo,
            text="Relatorio PMD",
            font=("Arial", 20, "bold"),
            text_color=cor.DHL_COLORS["text_light"]
        )
        label_titulo_frame.pack(side="left", padx=20)

        #botao de selecao
        self.select_button = ctk.CTkSegmentedButton(
            self.frame_titulo,
            height=60,
            values=["Normais", "Fines", "STS"],
            text_color=cor.DHL_COLORS["text_light"],
            fg_color=cor.DHL_COLORS["gray_dark"],
            command=self.selecionar
        )
        self.select_button.pack(side="right", padx=20)


        # ------------------ header ------------------------

        #-------------------- Frame Esquerdo ----------------

        self.frame_esquerdo = ctk.CTkScrollableFrame(
            self.frame_conteiner,
            width=400,
            border_color=cor.DHL_COLORS["gray_dark"],
            border_width=3
        )
        self.frame_esquerdo.pack(fill="y", side="left", anchor="center", padx=5, pady=10)

        

        #-------------------- Frame Esquerdo ----------------


        #-------------------- Frame Direito ----------------

        self.frame_direito = ctk.CTkScrollableFrame(
            self.frame_conteiner,
            width=1100,
            border_color=cor.DHL_COLORS["gray_dark"],
            border_width=3
        )
        self.frame_direito.pack(fill="y", side="left", anchor="center", padx=5, pady=10)

        #-------------------- Frame Direito ----------------

        #--------------------- Construcao Primaria --------------------




    def selecionar(self, values):
        print(values)
        limpar_frame(self.frame_esquerdo)
        limpar_frame(self.frame_direito)
        self.frame_direito.configure(label_text = "")
        core.listar_misturas(values, self.frame_esquerdo, self.frame_direito)