#FUncoes uteis para o código
#Criador: Marcus Vinicius Hilário de Oliveira
#Data: 27/07/2025

import customtkinter as ctk

def limpar_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()
