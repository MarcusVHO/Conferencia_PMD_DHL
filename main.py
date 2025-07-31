#Rsponsavel pela criacao do aplicativo principal
#Criador: Marcus Vinicius Hilário de Oliveira
#Data: 25/07/2025

#------------------ inportações Externas --------------------
import customtkinter as ctk
#------------------ inportações Externas --------------------

#------------------ inportações internas --------------------
import config.colors as cor
import config.settings as st

from core.navigation import NavigationManager
from view.login_view import Login
from view.home_view import Home
from view.pmd.pmd_home_view import Pmd
from view.pmd.inserir_mistura_view import Insert_Mist
from view.pmd.menu_conferencia_view import Conferencia_Pmd_Menu
from view.pmd.seletor_de_op_view import Seletor_de_Op
from view.pmd.conferir_mistura_view import Conferir_Mistura
from view.pmd.gerenciar_view import Gerenciar
from view.relatorio.menu_relatorio_view import Home_Report
#------------------ inportações internas --------------------



#aparencia do sistema
ctk.set_appearance_mode(st.APP_THEME)

#frame criador do app
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title(st.APP_TITLE)
        self.geometry(st.APP_SIZE)
        self.iconbitmap(st.APP_ICO)
        self.navigator = NavigationManager(self)

        # Carrega primeira tela
        self.show_login()


    #comando criador tela de login
    def show_login(self):
        self.navigator.show_frame(lambda master=self: Login(master, navigate_to_home=self.show_home))

    #comando criador tela inicial
    def show_home(self):
        self.navigator.show_frame(lambda master=self: Home(master, navigate_to_pmd=self.show_PMD, navigate_to_login=self.show_login, navigate_to_report=self.show_report))




    #comando criador menu PMD
    def show_PMD(self):
        self.navigator.show_frame(lambda master=self: Pmd(master, navigate_to_home=self.show_home, navigate_to_inserir_misturas=self.show_insert_mist, navigate_to_conferencia_pmd=self.show_conferencia_pmd, navigate_to_gerenciar=self.show_gerenciar_pmd))

    #comando criador tela de inserir misturas do PMD
    def show_insert_mist(self):
        self.navigator.show_frame(lambda master=self: Insert_Mist(master, navigate_to_home_pmd=self.show_PMD))

    #camada criadora do submenu de conferencia
    def show_conferencia_pmd(self):
        self.navigator.show_frame(lambda master=self: Conferencia_Pmd_Menu(master, navigate_to_home_pmd=self.show_PMD, navigate_to_seletor_de_op=self.show_seletor_de_op))

    #show seletor de op
    def show_seletor_de_op(self, tipo_de_conferencia):
        self.navigator.show_frame(lambda master=self: Seletor_de_Op(master, tipo_de_conferencia, navigate_to_menu_conferencia=self.show_conferencia_pmd, conferir_mistura=self.show_conferir_mistura))

    #show conferir mistura
    def show_conferir_mistura(self, op, tipo_de_conferencia):
        self.navigator.show_frame(lambda master=self: Conferir_Mistura(master, op, navigate_to_seletor_de_op=self.show_seletor_de_op, tipo_de_conferencia=tipo_de_conferencia))

    #tela de gerenciamento pmd
    def show_gerenciar_pmd(self):
        self.navigator.show_frame(lambda master=self: Gerenciar(master, navigate_to_home_pmd=self.show_PMD))
    




    def show_report(self):
        self.navigator.show_frame(lambda master=self: Home_Report(master, navigate_to_home=self.show_home))
    



if __name__ == "__main__":
    app = App()
    app.mainloop()
