from screens.tela_inicial import Tela_Inicial
from screens.Conferencia_PMD.menu_conferencia import Menu_Conferencia
from screens.Conferencia_PMD.conferencia_misturas import Conferencia_Misturas
from screens.Conferencia_PMD.conferencia_fines import Conferencia_Fines
import customtkinter as ctk
import config

class Sistema_DHL(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title(config.APP_TITLE)
        self.geometry(config.APP_SIZE)
        self.conteiner_frame = None
        self.mostrar_tela_inicial()
        self.iconbitmap(config.APP_ICO)
        self.corner_radius=False
        self.fg_color=config.CORES["primaria"]
    def limpar(self):
        if self.conteiner_frame is not None:
            self.conteiner_frame.pack_forget()
            self.conteiner_frame.destroy()
            self.conteiner_frame = None

    def mostrar_tela_inicial(self, event=None):
        self.limpar()
        self.tela_inicial = Tela_Inicial(self, self.mostrar_menu_conferencia)
        self.conteiner_frame = self.tela_inicial.frame
        self.conteiner_frame.pack(fill="both", expand=True)

    def mostrar_menu_conferencia(self, event=None):
        self.limpar()
        self.menu_conferncia = Menu_Conferencia(self, self.mostrar_conferencia_misturas, self.mostrar_tela_inicial, self.mostrar_conferencia_fines)
        self.conteiner_frame = self.menu_conferncia.frame
        self.conteiner_frame.pack(fill="both", expand=True)

    def mostrar_conferencia_misturas(self, event=None):
        self.limpar()
        self.conferencia_misturas = Conferencia_Misturas(self, self.mostrar_menu_conferencia)
        self.conteiner_frame = self.conferencia_misturas.frame
        self.conteiner_frame.pack(fill="both", expand=True)

    def mostrar_conferencia_fines(self, event=None):
        self.limpar()
        self.conferencia_misturas = Conferencia_Fines(self, self.mostrar_menu_conferencia)
        self.conteiner_frame = self.conferencia_misturas.frame
        self.conteiner_frame.pack(fill="both", expand=True)

if __name__ == "__main__":
    app = Sistema_DHL()
    app.mainloop()