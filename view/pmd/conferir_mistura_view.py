#Responsavel por criar elementos visuais da conferencia de misturas
#Criador: Marcus Vinicius Hilário de Oliveira
#Data: 28/07/2025


#------------------ inportações Externas --------------------
import customtkinter as ctk
#------------------ inportações Externas --------------------


#------------------ inportações Internas --------------------
import config.colors as cor
import core.pmd.conferir_mistura_controller as core
from view.components.screen_components import *
#------------------ inportações Internas --------------------


class Conferir_Mistura(ctk.CTkFrame):
    def __init__(self, master, op, navigate_to_seletor_de_op):

        #inicializacao primaria
        super().__init__(master)
        self.navigate_to_seletor_de_op=navigate_to_seletor_de_op

        #inicializacao de variaveis
        self.op = op
        self.confimados = 0
        self.total = 0
        self.progresso_da_barra = 0
        self.misturas = 0
        self.mistura_atual = 0

        #frame principal
        self.frame = ctk.CTkFrame(self, fg_color=cor.DHL_COLORS["primary"])
        self.frame.pack(fill="both", expand=True)

        #inicializacao de cabecalho e rodape
        Cabecalho(self.frame, "Conferir Mistura")
        rodape = Rodape(self.frame, True, self.voltar)
        rodape.entry_OPT.destroy()
        rodape.label_OPT.destroy()

        #verifica status da op antes de construir
        self.atualizar_dados()


        #frame que ira conter itens
        self.frame_conteiner = ctk.CTkFrame(
            self.frame,
            fg_color= "transparent"

        )
        self.frame_conteiner.pack(fill="both", expand=True)
        self.frame_conteiner.pack_propagate(False)
        self.frame_conteiner.grid_propagate(False)

        #configuracao de frame 
        for i in range(5):
            self.frame_conteiner.grid_rowconfigure(i, weight=1)
            self.frame_conteiner.grid_columnconfigure(i, weight=1)



        # --------------- Frame Esquerdo ---------------------

        frame_esquerdo = ctk.CTkFrame(
            self.frame_conteiner,
            width=400,
            border_color=cor.DHL_COLORS["gray_dark"],
            border_width=5
        )
        frame_esquerdo.grid(row=0, column=0, rowspan=3)


        #titulo_mistura
        titulo_mistura_tabela_esquerda = ctk.CTkLabel(
            frame_esquerdo,
            text="MISTURA",
            text_color=cor.DHL_COLORS["text_light"],
            fg_color=cor.DHL_COLORS["gray_dark"],
            height=60,
            width=400,
            font=("Arial", 20, "bold")
        )
        titulo_mistura_tabela_esquerda.pack(padx=5, pady=(5,0))

        #titulo
        OP_tabela_esquerda = ctk.CTkLabel(
            frame_esquerdo,
            text=f"OP: {op}",
            text_color=cor.DHL_COLORS["text_dark"],
            fg_color=cor.DHL_COLORS["gray_light"],
            height=100,
            width=400,
            font=("Arial", 20, "bold")
        )
        OP_tabela_esquerda.pack(padx=5)

        #itens_confirmados
        titulo_itens_confirmados_tabela_esquerda = ctk.CTkLabel(
            frame_esquerdo,
            text="ITENS CONFIRMADOS",
            text_color=cor.DHL_COLORS["text_light"],
            fg_color=cor.DHL_COLORS["gray_dark"],
            height=60,
            width=400,
            font=("Arial", 20, "bold")
        )
        titulo_itens_confirmados_tabela_esquerda.pack(padx=5)       
        
        #label intesn cofirmaods
        self.itens_confirmados_tabela_esquerda = ctk.CTkLabel(
            frame_esquerdo,
            text=f" {self.confimados} / {self.total}",
            text_color=cor.DHL_COLORS["text_dark"],
            fg_color=cor.DHL_COLORS["gray_light"],
            height=100,
            width=400,
            font=("Arial", 20, "bold")
        )
        self.itens_confirmados_tabela_esquerda.pack(padx=5)
        
        #titulo progresso
        titulo_progresso_tabela_esquerda = ctk.CTkLabel(
            frame_esquerdo,
            text="PROGRESSO",
            text_color=cor.DHL_COLORS["text_light"],
            fg_color=cor.DHL_COLORS["gray_dark"],
            height=60,
            width=400,
            font=("Arial", 20, "bold")
        )
        titulo_progresso_tabela_esquerda.pack(padx=5)       
        
        #barra de progresso
        self.frame_barra = ctk.CTkFrame(frame_esquerdo, height=100, width=400 , fg_color=cor.DHL_COLORS["gray_light"], corner_radius=False)
        self.barra_de_progresso = ctk.CTkProgressBar(
            self.frame_barra,
            orientation="horizontal",
            progress_color=cor.DHL_COLORS["secondary"],
            mode="determinate",
            height=20,
            fg_color=cor.DHL_COLORS["gray_medium"],
            bg_color=cor.DHL_COLORS["gray_light"]
        )
        self.barra_de_progresso.pack(anchor="center", expand=True, fill="x", padx=10)
        self.barra_de_progresso.set(self.progresso_da_barra)
        self.frame_barra.pack(padx=5, pady=(0,5))      
        self.frame_barra.pack_propagate(False)

        # --------------- Frame Esquerdo ---------------------



        # --------------- Frame Central ---------------------

        #a confirmar frame
        self.frame_acofirmar = ctk.CTkFrame(
            self.frame_conteiner, 
            border_color=cor.DHL_COLORS["text_dark"], 
            border_width=2, 
            fg_color=cor.DHL_COLORS["gray_medium"]
        )
        self.frame_acofirmar.grid(row=2, column=2, padx=30, pady=(0, 5), sticky="n")

        #configuracoes do frame
        self.frame_acofirmar.grid_rowconfigure(0, weight=1)
        self.frame_acofirmar.grid_rowconfigure(1, weight=1)
        self.frame_acofirmar.grid_rowconfigure(2, weight=1)

        #texto titulo frame a confirmar
        self.label_titulo_frame_aconfirmar = ctk.CTkLabel(
            self.frame_acofirmar, 
            text="DHL - Misturas", 
            height=100, 
            font=("Arial", 50, "bold"), 
            text_color=cor.DHL_COLORS["text_light"], 
            fg_color=cor.DHL_COLORS["gray_dark"]
        )
        self.label_titulo_frame_aconfirmar.pack( padx=1, pady=1, fill="x")

        #a confirmar label texto
        self.label_confirmar = ctk.CTkLabel(
            self.frame_acofirmar, 
            text=self.mistura_atual, 
            height=100, width=400, 
            font=("Arial", 60, "bold"), 
            text_color=cor.DHL_COLORS["gray_dark"]
        )
        self.label_confirmar.pack(padx=5, pady=5, fill="x")

        #a confirmar entry 
        self.entry_aconfirmar = ctk.CTkEntry(
            self.frame_acofirmar, 
            height=70, 
            font=("Arial", 30)
        )
        self.entry_aconfirmar.pack(padx=15, pady=(5, 15), fill="x")
        self.entry_aconfirmar.focus()
        self.entry_aconfirmar.bind("<Return>", self.conferir_mistura)
        

        # --------------- Frame Central ---------------------


        # --------------- Frame Direito ---------------------

        #frame lista historico
        self.frame_lista_direita = ctk.CTkScrollableFrame(
                self.frame_conteiner, width=400, 
                corner_radius=False, 
                border_width=2, 
                border_color=cor.DHL_COLORS["gray_dark"], 
                label_text="CONFIRMADOS", 
                label_font=("Arial", 20, "bold"), 
                label_fg_color=cor.DHL_COLORS["gray_dark"],
                label_text_color=cor.DHL_COLORS["text_light"]
                )
        self.frame_lista_direita.grid(row=0, column=4, rowspan=4, padx=5, pady=20, sticky="ns")

        # --------------- Frame Direito ---------------------

    def atualizar_dados(self):
        self.dados = core.atualizar_dados(self.op, self.confimados)
        self.confimados = self.dados["confirmados"]
        self.total = self.dados["total"]
        self.progresso_da_barra = self.dados["confirmados"]/self.dados["total"]
        self.misturas = self.dados["misturas"]
        self.mistura_atual = self.dados["misturas"][self.confimados]

    def atualizar_dados_tela(self):
        self.itens_confirmados_tabela_esquerda.configure(text=f" {self.confimados} / {self.total}")
        self.barra_de_progresso.set(self.progresso_da_barra)
        self.label_confirmar.configure(text=self.mistura_atual)

    def conferir_mistura(self, event=None):
        texto_digitado = self.entry_aconfirmar.get().strip()
        resposta = core.conferir_mistura(self.op, self.mistura_atual, texto_digitado, self.confimados)
        if resposta == True:
            self.atualizar_dados()
            self.atualizar_dados_tela()
   
    def voltar(self, event=None):
        self.navigate_to_seletor_de_op("mistura_normal")
