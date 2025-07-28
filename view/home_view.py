#Tela inicial do sistema
#Criador: Marcus Vinicius Hilário de Oliveira
#Data: 25/07/2025


#------------------ inportações Externas --------------------
import customtkinter as ctk
from PIL import Image
#------------------ inportações Externas --------------------


#------------------ inportações internas --------------------
import config.colors as cor
from view.components.screen_components import *
#------------------ inportações internas --------------------




#------------------ Classe pincipal --------------------
class Home(ctk.CTkFrame):
    def __init__(self, master, navigate_to_pmd):

        #inicializacao primaria
        super().__init__(master)
        self.navigation_to_pmd = navigate_to_pmd

        #ciracao frame principal
        self.frame = ctk.CTkFrame(self, fg_color=cor.DHL_COLORS["primary"])
        self.frame.pack(fill="both", expand=True)

        #inicializacao de imagens
        self.img_carretinha = ctk.CTkImage(light_image=Image.open(st.APP_IMG_CARRETINHA), size=(150,150))
        self.img_transpalete = ctk.CTkImage(light_image=Image.open(st.APP_IMG_TRANSPALETE), size=(150,150))
        self.img_carreta = ctk.CTkImage(light_image=Image.open(st.APP_IMG_CARRETA), size=(150,150))

        #inicializacao cabecalho 
        Cabecalho(self.frame, "HOME")
        

        #-------construcao pincipal------

        #botaão PMD
        self.botao_pmd = botao(self.frame, self.img_carretinha, "   1 - PMD   ", navigate_to_pmd)
        self.botao_pmd.frame_button.pack(side="left",anchor="n", padx=20, pady=20)

        #botaão pedagio
        self.botao_pedagio = botao(self.frame, self.img_transpalete, "   2 - PEDÁGIO   ", None)
        self.botao_pedagio.frame_button.pack(side="left",anchor="n", padx=20, pady=20)

        #botaão Recebimento
        self.botao_Recebimento = botao(self.frame, self.img_carreta, "   3 - RECEBIMENTO   ", None)
        self.botao_Recebimento.frame_button.pack(side="left",anchor="n", padx=20, pady=20)

        
        #-------construcao pincipal------



        #inicialização rodapé
        Rodape(self, False, None)