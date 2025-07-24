from screens.login import Login
from screens.menu_inicial import Tela_Inicial
from screens.Conferencia_PMD.menu_conferencia import Menu_Conferencia
import customtkinter as ctk
import config

class Sistema_DHL(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title(config.APP_TITLE)
        self.geometry(config.APP_SIZE)
        self.conteiner_frame = None
        self.iconbitmap(config.APP_ICO)
        self.corner_radius=False
        self.fg_color=config.CORES["primaria"]
        self.mostrar_tela_login()


    #limpa tela exibida atualmente
    def limpar(self, event=None):
        if self.conteiner_frame is not None:
            self.conteiner_frame.pack_forget()
            self.conteiner_frame.destroy()
            self.conteiner_frame = None

    #cira tela de login
    def mostrar_tela_login(self, event=None):
        self.limpar()
        self.tela_login = Login(self, self.mostrar_tela_inicial)
        self.conteiner_frame = self.tela_login.frame
        self.conteiner_frame.pack(fill="both", expand=True)

    #cira o menu inicial
    def mostrar_tela_inicial(self, event=None):
        self.limpar()
        self.tela_inicial = Tela_Inicial(self, self.mostrar_menu_conferencia)
        self.conteiner_frame = self.tela_inicial.frame
        self.conteiner_frame.pack(fill="both", expand=True)

    #cria menu conferencia pmd
    def mostrar_menu_conferencia(self, event=None):
        self.limpar()
        self.menu_conferncia = Menu_Conferencia(self, self.mostrar_tela_inicial, self.limpar, self.mostrar_menu_conferencia)
        self.conteiner_frame = self.menu_conferncia.frame
        self.conteiner_frame.pack(fill="both", expand=True)

    
if __name__ == "__main__":
    app = Sistema_DHL()
    app.mainloop()