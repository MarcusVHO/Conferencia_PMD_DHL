#Responsavel pela navegacao do sistema
#Criador: Marcus Vinicius Hilário de Oliveira
#Data: 25/07/2025


#------------------ inportações Externas --------------------
import customtkinter as ctk
#------------------ inportações Externas --------------------

#------------------ inportações internas --------------------
#------------------ inportações internas --------------------


# ---------------------- Classe principal ------------------
class NavigationManager:
    def __init__(self, root):
        self.root = root
        self.current_frame = None

    def show_frame(self, frame_class):
        # Destroi o frame atual (se houver)
        if self.current_frame is not None:
            self.current_frame.destroy()

        # Cria e exibe a nova tela
        self.current_frame = frame_class(self.root)
        self.current_frame.pack(fill="both", expand=True)
