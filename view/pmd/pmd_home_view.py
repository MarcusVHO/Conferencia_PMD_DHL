#Menu principal pmd
#Criador: Marcus Vinicius Hilário de Oliveira
#Data: 26/07/2025


#------------------ inportações Externas --------------------
import customtkinter as ctk
from PIL import Image
import winsound
#------------------ inportações Externas --------------------


#------------------ inportações internas --------------------
import config.colors as cor
from view.components.screen_components import *
#------------------ inportações internas --------------------




#------------------ Classe pincipal --------------------
class Pmd(ctk.CTkFrame):
    def __init__(self, master, navigate_to_home, navigate_to_inserir_misturas, navigate_to_conferencia_pmd, navigate_to_gerenciar):

        #inicializacao primaria
        super().__init__(master)
        self.navigation_to_home = navigate_to_home
        self.navigation_to_inserir_misturas = navigate_to_inserir_misturas
        self.navigate_to_conferencia_pmd = navigate_to_conferencia_pmd
        self.navigate_to_gerenciar = navigate_to_gerenciar

        #ciracao frame principal
        self.frame = ctk.CTkFrame(self, fg_color=cor.DHL_COLORS["primary"])
        self.frame.pack(fill="both", expand=True)

        #inicializacao de imagens
        self.img_coletor = ctk.CTkImage(light_image=Image.open(st.APP_IMG_COLETOR), size=(150,150))
        self.img_clamps = ctk.CTkImage(light_image=Image.open(st.APP_IMG_CLAMPS), size=(150,150))
        self.img_engrangem = ctk.CTkImage(light_image=Image.open(st.APP_IMG_ENGRENAGEM), size=(150,150))

        #inicializacao cabecalho 
        Cabecalho(self.frame, "PMD")
        

        #-------construcao pincipal------

        #botaão PMD
        self.botao_conferencia = botao(self.frame, self.img_coletor, "   1 - CONFERENCIA   ", self.ir_para_conferencia_pmd)
        self.botao_conferencia.frame_button.pack(side="left",anchor="n", padx=20, pady=20)

        #botaão Adicionar mistura
        self.botao_adicionar_mistura = botao(self.frame, self.img_clamps, "   2 - ADICIONAR MISTURA   ", self.ir_para_inserir_misturas)
        self.botao_adicionar_mistura.frame_button.pack(side="left",anchor="n", padx=20, pady=20)

        #botaão gerenciar
        self.botao_adicionar_mistura = botao(self.frame, self.img_engrangem, "   3 - GERENCIAR   ", command=self.ir_para_gerenciar_pmd)
        self.botao_adicionar_mistura.frame_button.pack(side="left",anchor="n", padx=20, pady=20)

        #-------construcao pincipal------

        


        #inicialização rodapé
        Rodape(self, True, self.navigation_to_home)



    def ir_para_inserir_misturas(self, event=None):
        self.navigation_to_inserir_misturas()

    def ir_para_conferencia_pmd(self, event=None):
        self.navigate_to_conferencia_pmd()

    def ir_para_gerenciar_pmd(self, event=None):
        if st.USUARIO_LOGADO["permissao"] in ["criador", "supervisor", "cordenador", "analista"]:
            self.navigate_to_gerenciar()
        else:
            winsound.MessageBeep(winsound.MB_ICONHAND)