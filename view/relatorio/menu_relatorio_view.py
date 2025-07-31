#Menu de relatorio
#Criador: Marcus Vinicius Hilário de Oliveira
#Data: 31/07/2025


#------------------ inportações Externas --------------------
import customtkinter as ctk
from PIL import Image
#------------------ inportações Externas --------------------


#------------------ inportações internas --------------------
import config.colors as cor
from view.components.screen_components import *
#------------------ inportações internas --------------------




#------------------ Classe pincipal --------------------
class Home_Report(ctk.CTkFrame):
    def __init__(self, master, navigate_to_home):

        #inicializacao primaria
        super().__init__(master)
        self.navigate_to_home = navigate_to_home

        #ciracao frame principal
        self.frame = ctk.CTkFrame(self, fg_color=cor.DHL_COLORS["primary"])
        self.frame.pack(fill="both", expand=True)

        #inicializacao de imagens
        self.img_pranchetea = ctk.CTkImage(light_image=Image.open(st.APP_IMG_PRANCHETA), size=(150,150))


        #inicializacao cabecalho 
        Cabecalho(self.frame, "RELATÓRIO")
        

        #-------construcao pincipal------

        #botaão PMD
        self.botao_pmd = botao(self.frame, self.img_pranchetea, "   1 - PMD   ", None)
        self.botao_pmd.frame_button.pack(side="left",anchor="n", padx=20, pady=20)

        #botaão pedagio
        self.botao_pedagio = botao(self.frame, self.img_pranchetea, "   2 - PEDÁGIO   ", None)
        self.botao_pedagio.frame_button.pack(side="left",anchor="n", padx=20, pady=20)

        #botaão Recebimento
        self.botao_Recebimento = botao(self.frame, self.img_pranchetea, "   3 - RECEBIMENTO   ", None)
        self.botao_Recebimento.frame_button.pack(side="left",anchor="n", padx=20, pady=20)

        
        #-------construcao pincipal------



        #inicialização rodapé
        Rodape(self, True, self.navigate_to_home)
