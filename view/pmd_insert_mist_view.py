#Responsavel por introduzir os pefs no sistema
#Criador: Marcus Vinicius Hilário de Oliveira
#Data: 26/07/2025

#------------------ inportações Externas --------------------
import customtkinter as ctk
from PIL import Image
#------------------ inportações Externas --------------------

#------------------ inportações internas --------------------
import config.settings as st
import config.colors as cor
import view.components.widgets_reutilizaveis as alerts
from view.components.screen_components import *
import core.pmd_insert_mist_controller as core
from utils.utilities import *
#------------------ inportações internas --------------------


#classe primaria
class Insert_Mist(ctk.CTkFrame):
    def __init__(self, master, navigate_to_home_pmd):

        #inicializacao primaria
        super().__init__(master)
        self.navigate_to_home_pmd = navigate_to_home_pmd

        #contrucao frame principal
        self.frame = ctk.CTkFrame(self, fg_color=cor.DHL_COLORS["primary"])
        self.frame.pack(fill="both", expand=True)

        #inicializacao de variaveis
        self.variavel_seletor_tipo = None
        self.type = None

        #inicializacao cabecalho
        Cabecalho(self.frame, "ADICIONAR MISTURA")


        #---- construcao primaria ----

        #frame que ira conter outros intens
        self.frame_conteiner = ctk.CTkFrame(self.frame, width=(1200))
        self.frame_conteiner.pack(side="left", fill="y", expand=True, padx=20, pady=20)
        self.frame_conteiner.pack_propagate(False)


        #cabecalho do frame conteiner
        frame_titulo = ctk.CTkFrame(
            self.frame_conteiner, 
            fg_color=cor.DHL_COLORS["gray_dark"], 
            height=70
        )
        frame_titulo.pack(anchor="n", side="top", fill="x")
        frame_titulo.pack_propagate(False)
        
        #texto titulo do frame conteiner
        texto_titulo = ctk.CTkLabel(
            frame_titulo, 
            text="INSERSOR DE MISTURAS",
            text_color=cor.DHL_COLORS["text_light"],
            font=("Arial", 30, "bold")
        )
        texto_titulo.pack(anchor="center", side="left", padx=20)


        #botao segmentado do cabecalho
        self.seletor_tipo = ctk.CTkSegmentedButton(
            frame_titulo, 
            height=40, 
            fg_color=cor.DHL_COLORS["gray_dark"],
            bg_color=cor.DHL_COLORS["gray_dark"],
            font=("Arial", 20),
            values=["Normais", "STS"],
            unselected_color=cor.DHL_COLORS["gray_dark"],
            selected_color=cor.DHL_COLORS["gray_medium"],
            command=self.selecionar_tipo
        )
        self.seletor_tipo.pack(side="right", padx=20)



        #frame que tera a visualizacao das misturas adicionadas
        self.frame_central = ctk.CTkScrollableFrame(
            self.frame_conteiner,
        )
        self.frame_central.pack(side="top", fill="both", expand=True, padx=20, pady=10)


        #rodape do frame conteiner
        self.frame_rodape = ctk.CTkFrame(
            self.frame_conteiner,
            fg_color=cor.DHL_COLORS["gray_dark"],
            height=70
        )
        self.frame_rodape.pack(side="bottom", anchor="s", fill="x")
        self.frame_rodape.pack_propagate(False)

    
        self.botao_voltar = ctk.CTkButton(    
            self.frame_rodape,
            height=40,
            text="VOLTAR",
            fg_color=cor.DHL_COLORS["gray_light"],
            text_color=cor.DHL_COLORS["text_dark"],
            font=("Arial", 20, "bold"),
            command=self.voltar,
            
        )
        self.botao_voltar.pack(side="left", anchor="center", padx=20)


        #botao atualizador de tela
        self.botao_atualizar = ctk.CTkButton(    
            self.frame_rodape,
            height=40,
            text="ATUALIZAR",
            fg_color=cor.DHL_COLORS["gray_light"],
            text_color=cor.DHL_COLORS["text_dark"],
            font=("Arial", 20, "bold"),
            command=self.atualizar_tela,
            
        )
        self.botao_atualizar.pack(side="left", anchor="center", padx=20)

        #frame dinamico
        self.frame_botoes_dinamicos = ctk.CTkFrame(self.frame_rodape, fg_color="transparent")
        self.frame_botoes_dinamicos.pack(side="right", anchor="center")



    #respnsavel por contruir intens dentro do frame central
    def selecionar_tipo(self,value, event=None):

        print("Opcao selecionada -> ", value)
        self.type = value

        if value == "Normais":
            limpar_frame(self.frame_central)
            core.mostrar_misturas_normais(self.frame_central)
            self.criar_botao_mistura_normal()
            
        elif value == "STS":
            limpar_frame(self.frame_central)
            core.mostrar_sts(self.frame_central)
            self.criar_botao_sts()


    #cria botaão que adicionara mistura normal
    def criar_botao_mistura_normal(self):
        limpar_frame(self.frame_botoes_dinamicos)
        botao_mistura_normal = ctk.CTkButton(
            self.frame_botoes_dinamicos, 
            height=40, 
            width=200, 
            text="ADIC MISTURA NORMAL", 
            font=("Arial", 20, "bold"), 
            text_color=cor.DHL_COLORS["text_dark"],
            fg_color=cor.DHL_COLORS["gray_light"],
            hover_color=cor.DHL_COLORS["gray_dark"],
            command=core.selecionar_arquivo_misturas_normais
        )
        botao_mistura_normal.pack(side="right", anchor="center", padx=20)

    #cria botao que adcionara sts
    def criar_botao_sts(self):
        limpar_frame(self.frame_botoes_dinamicos)
        botao_sts = ctk.CTkButton(
            self.frame_botoes_dinamicos, 
            height=40, 
            width=200, 
            text="  ADIC STS  ", 
            font=("Arial", 20, "bold"), 
            text_color=cor.DHL_COLORS["text_dark"],
            fg_color=cor.DHL_COLORS["gray_light"],
            hover_color=cor.DHL_COLORS["gray_dark"],
            command=core.selecionar_arquivo_sts
        )
        botao_sts.pack(side="right", anchor="center", padx=20)


    #atualiza intens na tela
    def atualizar_tela(self, event=None):
        if self.type == "Normais":
            limpar_frame(self.frame_central)
            core.mostrar_misturas_normais(self.frame_central)

        elif self.type == "STS":
           limpar_frame(self.frame_central)
           core.mostrar_sts(self.frame_central)

        else:
            print("Selecione tipo antes!! ")



    def voltar(self, event=None):
        self.navigate_to_home_pmd()
