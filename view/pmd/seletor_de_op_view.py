#Responsavel por selecionar a op que sera direcionada a conferencia 
#Criador: Marcus Vinicius Hilário de Oliveira
#Data: 27/07/2025


#------------------ inportações Externas --------------------
import customtkinter as ctk
#------------------ inportações Externas --------------------


#------------------ inportações Internas --------------------
import config.colors as cor
import core.pmd.seletor_de_op_controller as core
from view.components.screen_components import *
#------------------ inportações Internas --------------------



#Classe primaria da tela
class Seletor_de_Op(ctk.CTkFrame):
    def __init__(self, master, tipo_de_conferencia, navigate_to_menu_conferencia, conferir_mistura):

        #inicializacao primaria
        super().__init__(master)
        self.master = master

        #inicializacao de variaveis
        self.tipo_de_conferencia = tipo_de_conferencia
        self.navigate_to_menu_conferencia = navigate_to_menu_conferencia
        self.conferir_mistura = conferir_mistura
        #criacao do frame principal
        self.frame = ctk.CTkFrame(
            self,
            fg_color=cor.DHL_COLORS["primary"]
        )
        self.frame.pack(fill="both", expand=True)


        #------------- Ciracao Principal -------------

        #inicializacao de cabecalho
        Cabecalho(self.frame, "Seletor de OP")
        
        #inicializacao de rodape
        rodape = Rodape(self.frame, True, lambda: self.navigate_to_menu_conferencia())
        rodape.entry_OPT.destroy()
        rodape.label_OPT.destroy()
        
        #frame que ira conter intens
        self.frame_conteiner= ctk.CTkFrame(
            self.frame,
            fg_color=cor.DHL_COLORS["gray_medium"],
            width=1000
        )
        self.frame_conteiner.pack(fill="y", expand=True, padx=40, pady=20)
        self.frame_conteiner.pack_propagate(False)



        #cabecalho do frame conteiner
        self.header_frame_conteiner = ctk.CTkFrame(
            self.frame_conteiner,
            fg_color=cor.DHL_COLORS["gray_dark"],
            height=70
        )
        self.header_frame_conteiner.pack(fill="x", side="top")
        self.header_frame_conteiner.pack_propagate(False)

        #titulo header
        self.titulo_header = ctk.CTkLabel(
            self.header_frame_conteiner,
            text="Selecionar a OP: ",
            text_color=cor.DHL_COLORS["text_light"],
            font=("Arial", 30, "bold")
        )
        self.titulo_header.pack(side="left", anchor="center", padx=20)


        #Frame central
        self.frame_central = ctk.CTkScrollableFrame(
            self.frame_conteiner,
            fg_color=cor.DHL_COLORS["gray_light"]
        )
        self.frame_central.pack(fill="both", expand=True, padx=20, pady=20)


        #frame rodape
        self.footer_frame_conteiner = ctk.CTkFrame(
            self.frame_conteiner,
            height=70,
            fg_color=cor.DHL_COLORS["gray_dark"],
        )
        self.footer_frame_conteiner.pack(fill="x", side="bottom")
        self.footer_frame_conteiner.pack_propagate(False)

        #descricao do campo de entrada
        self.texto_footer = ctk.CTkLabel(
            self.footer_frame_conteiner,
            text="OP: ",
            font=("Arial", 20, "bold"),
            text_color=cor.DHL_COLORS["text_light"]
        )
        self.texto_footer.pack(side="left", anchor="center", padx=(50,0))

        #entry de op manual
        self.entry_op_manual = ctk.CTkEntry(
            self.footer_frame_conteiner,
            placeholder_text="INSIRA A OP AQUI",
            height=40, 
            width=200,
        )
        self.entry_op_manual.pack(side="left", anchor="center", padx=10)
        self.after(100, lambda: self.entry_op_manual.focus_set())

        self.criar_botoes()


    def criar_botoes(self):
        core.criar_botoes(self.frame_central, self.tipo_de_conferencia, self.conferir_mistura)        

    