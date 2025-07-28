#Menu de conferenica do pmd
#Criador: Marcus Vinicius Hilário de Oliveira
#Data: 27/07/2025


#------------------ inportações Externas --------------------
import customtkinter as ctk
from PIL import Image
#------------------ inportações Externas --------------------


#------------------ inportações internas --------------------
import config.colors as cor
from view.components.screen_components import *
#------------------ inportações internas --------------------




#------------------ Classe pincipal --------------------
class Conferencia_Pmd_Menu(ctk.CTkFrame):
    def __init__(self, master, navigate_to_home_pmd, navigate_to_seletor_de_op):

        #inicializacao primaria
        super().__init__(master)
        self.navigation_to_home_pmd = navigate_to_home_pmd
        self.navigate_to_seletor_de_op = navigate_to_seletor_de_op

        #ciracao frame principal
        self.frame = ctk.CTkFrame(self, fg_color=cor.DHL_COLORS["primary"])
        self.frame.pack(fill="both", expand=True)

        #inicializacao de imagens
        self.img_caixa_c48 = ctk.CTkImage(light_image=Image.open(st.APP_IMG_CAIXA_C48), size=(150,150))

        #inicializacao cabecalho 
        Cabecalho(self.frame, "PMD")
        

        #-------construcao pincipal------

        #botaão PMD
        self.botao_conferencia = botao(self.frame, self.img_caixa_c48, "   1 - CONFERIR MISTURA NORMAL   ", command= lambda: self.ir_para_seletor_de_op("mistura_normal"))
        self.botao_conferencia.frame_button.pack(side="left",anchor="n", padx=20, pady=20)


        self.botao_conferencia = botao(self.frame, self.img_caixa_c48, "   1 - CONFERIR FINES   ", command= lambda: self.ir_para_seletor_de_op("fines"))
        self.botao_conferencia.frame_button.pack(side="left",anchor="n", padx=20, pady=20)


        self.botao_conferencia = botao(self.frame, self.img_caixa_c48, "   1 - CONFERIR STS   ", command= lambda: self.ir_para_seletor_de_op("sts"))
        self.botao_conferencia.frame_button.pack(side="left",anchor="n", padx=20, pady=20)

       

        #-------construcao pincipal------

        


        #inicialização rodapé
        Rodape(self, True, self.navigation_to_home_pmd)


    def ir_para_seletor_de_op(self, tipo, event=None):
        self.navigate_to_seletor_de_op(tipo)



