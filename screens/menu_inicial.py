#Responsabel por ser a interface principal do app
#Criandor: Marcus Vinicius Hilário de Oliveira
#DATA: 15/07/2025
import customtkinter as ctk
from PIL import Image
import datetime
import sys
import os 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import config
import utils.funcoes as func
import utils.ultilitario_interface as interface

class Tela_Inicial():
    def __init__(self, app, callback_troca_tela_menu_misturas):
        self.app = app
        self.callback_troca_tela_menu_misturas = callback_troca_tela_menu_misturas
        self.frame = ctk.CTkFrame(self.app, corner_radius=False)

        cabecalho = interface.Cabecalho(self.frame, "SISTEMA DE APOIO OPERACIONAL")
        


        #Area de Botões
        self.area_botoes = ctk.CTkFrame(
           self.frame,
            height=100,
            fg_color=config.CORES["primaria"], 
            corner_radius=False
        )
        self.area_botoes.pack(side="top", fill="both", expand=True)

        #Botão Conferencia 
        self.botao_conferencia = ctk.CTkFrame(self.area_botoes, height=100, width=200, fg_color="white",corner_radius=5)
        self.botao_conferencia.pack(side="left", anchor="nw", padx=10, pady=10)
        self.label_conferencia = ctk.CTkLabel(
            self.botao_conferencia, 
            text="1",
            font=("Arial", 20),
            width=50,
            height=50,
            text_color=config.CORES["fundo"],
            fg_color=config.CORES["texto"])
        self.label_conferencia.pack(side="left", fill="both", expand=True)

        self.botao_conferencia_btn = ctk.CTkButton(
            self.botao_conferencia, 
            text="CONFERÊNCIA PMD", 
            height=90,
            width=190, 
            fg_color=config.CORES["fundo"], 
            hover_color=config.CORES["borda"],
            font=("Arial", 20),
            text_color=config.CORES["texto"],
            command= self.ir_para_menu_misturas,
            corner_radius=0)
        self.botao_conferencia_btn.pack(fill="both", expand=True, padx=5)

        #Botão Relatório 
        self.botao_relatório = ctk.CTkFrame(self.area_botoes, height=100, width=200, fg_color="white",corner_radius=5)
        self.botao_relatório.pack(side="left", anchor="nw", padx=10, pady=10)
        self.label_relatório = ctk.CTkLabel(
            self.botao_relatório, 
            text="2",
            font=("Arial", 20),
            width=50,
            height=50,
            text_color=config.CORES["fundo"],
            fg_color=config.CORES["texto"])
        self.label_relatório.pack(side="left", fill="both", expand=True)

        self.botao_relatório_btn = ctk.CTkButton(
            self.botao_relatório, 
            text="RELATÓRIO", 
            height=90,
            width=190, 
            fg_color=config.CORES["fundo"], 
            hover_color=config.CORES["borda"],
            font=("Arial", 20),
            text_color=config.CORES["texto"]
            )
        self.botao_relatório_btn.pack(fill="both", expand=True)

        #inicializaão rodapé
        self.rodape = interface.Rodape(self.frame, False, False)
        self.rodape.entry_OPT.bind("<Return>",self.opt)

        
    def ir_para_menu_misturas(self, event=None):
        self.callback_troca_tela_menu_misturas()


    def atualizar_relogio(self):
        agora = datetime.datetime.now().strftime("%H:%M:%S")
        self.label_relogio.configure(text=agora)
        self.frame.after(1000, self.atualizar_relogio)

    def opt(self, event=None):
        
        opcao = self.rodape.entry_OPT.get().strip()

        if opcao == "1":
            self.rodape.entry_OPT.delete(0, "end")
            self.ir_para_menu_misturas()

        elif opcao =="2":
            self.rodape.entry_OPT.delete(0, "end")
            return
        
        else:
            self.rodape.entry_OPT.delete(0, "end")




