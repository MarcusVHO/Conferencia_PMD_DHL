import sys
import os 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import config

import customtkinter as ctk
from PIL import Image
import datetime
from Conferencia_PMD.Conferencia_misturas.conferencia_misturas import Conferencia_Misturas
from Conferencia_PMD.Conferencia_sts.conferencia_sts import Conferencia_STS
from Conferencia_PMD.Conferencia_fines.conferencia_fines import Conferencia_Fines
import winsound
import utils.ultilitario_interface as interface
import utils.funcoes as func

class Menu_Conferencia():
    def __init__(self, app, voltar, limpar, mostra_menu_conferencia):
        self.app = app
        self.callback_troca_tela_misturas_normais = Conferencia_Misturas
        self.frame = ctk.CTkFrame(self.app, fg_color=config.CORES["primaria"],corner_radius=False)
        self.voltar = voltar
        self.ir_para_fines = Conferencia_Fines
        self.ir_para_sts = Conferencia_STS
        self.limpar_tela = limpar
        self.mostrar_menu_conferencia = mostra_menu_conferencia
        
        #inicialização cabecalho
        cabecalho = interface.Cabecalho(self.frame, "MENU CONFERENCIA")

        #Area de Botões
        self.area_botoes = ctk.CTkFrame(
            self.frame,
            height=100,
            fg_color=config.CORES["primaria"],
            corner_radius=False
        )
        self.area_botoes.pack(side="top", fill="both", expand=True)

       #Botão Conferir Misturas 
        self.botao_conferir_misturas = ctk.CTkFrame(self.area_botoes, height=100, width=200, fg_color=config.CORES["primaria"],corner_radius=5, border_color=config.CORES["texto"], border_width=2)
        self.botao_conferir_misturas.pack(side="top", padx=10, pady=2, fill="x", expand=True)
        self.label_conferir_misturas = ctk.CTkLabel(
            self.botao_conferir_misturas, 
            text="1",
            font=("Arial", 40),
            text_color=config.CORES["fundo"],
            bg_color=config.CORES["texto"],
            width=150,
            corner_radius=190)
        self.label_conferir_misturas.pack(side="left", pady=2, fill="y")

        self.botao_conferir_misturas_btn = ctk.CTkButton(
            self.botao_conferir_misturas, 
            text="CONFERIR MISTURAS", 
            height=90,
            width=190, 
            fg_color=config.CORES["fundo"], 
            hover_color=config.CORES["borda"],
            font=("Arial", 20),
            text_color=config.CORES["texto"],
            anchor="w",
            command=self.mostrar_conferencia_misturas,
            corner_radius=0)
        self.botao_conferir_misturas_btn.pack(side="left",padx=(0,1), pady=1, fill="both", expand=True)

        #Botão Conferir STS 
        self.botao_conferir_sts = ctk.CTkFrame(self.area_botoes, height=100, width=200, fg_color=config.CORES["primaria"],corner_radius=5, border_color=config.CORES["texto"], border_width=2)
        self.botao_conferir_sts.pack(side="top", padx=10, pady=2, fill="x", expand=True)
        self.label_conferir_sts = ctk.CTkLabel(
            self.botao_conferir_sts, 
            text="2",
            font=("Arial", 40),
            text_color=config.CORES["fundo"],
            bg_color=config.CORES["texto"],
            width=150,
            corner_radius=190)
        self.label_conferir_sts.pack(side="left", fill="y")
        self.botao_conferir_sts_btn = ctk.CTkButton(
            self.botao_conferir_sts, 
            text="CONFERIR STS", 
            height=90,
            width=190, 
            fg_color=config.CORES["fundo"], 
            hover_color=config.CORES["borda"],
            font=("Arial", 20),
            text_color=config.CORES["texto"],
            anchor="w",
            corner_radius=0,
            command=self.mostrar_conferencia_sts)
        self.botao_conferir_sts_btn.pack(side="left",padx=(0,1), pady=1, fill="both", expand=True)

        #Botão Conferir Fines 
        self.botao_conferir_fines = ctk.CTkFrame(self.area_botoes, height=100, width=200, fg_color=config.CORES["primaria"],corner_radius=5, border_color=config.CORES["texto"], border_width=2)
        self.botao_conferir_fines.pack(side="top", padx=10, pady=2, fill="x", expand=True)
        self.label_conferir_fines = ctk.CTkLabel(
            self.botao_conferir_fines, 
            text="3",
            font=("Arial", 40),
            text_color=config.CORES["fundo"],
            bg_color=config.CORES["texto"],
            width=150,
            corner_radius=190)
        self.label_conferir_fines.pack(side="left", fill="y")
        self.botao_conferir_fines_btn = ctk.CTkButton(
            self.botao_conferir_fines, 
            text="CONFERIR FINES", 
            height=90,
            width=190, 
            fg_color=config.CORES["fundo"], 
            hover_color=config.CORES["borda"],
            font=("Arial", 20),
            text_color=config.CORES["texto"],
            anchor="w",
            corner_radius=0,
            command=self.mostrar_conferencia_fines,
            )
        self.botao_conferir_fines_btn.pack(side="left",padx=(0,1), pady=1, fill="both", expand=True)




        #inicialização Rodapé
        self.rodape = interface.Rodape(self.frame, True, self.voltar)
        self.rodape.entry_OPT.bind("<Return>", self.opt)



    def atualizar_relogio(self):
        agora = datetime.datetime.now().strftime("%H:%M:%S")
        self.label_relogio.configure(text=agora)
        self.frame.after(1000, self.atualizar_relogio)

    #conferecia misturas
    def mostrar_conferencia_misturas(self, event=None):
        self.limpar_tela()
        self.conferencia_misturas = Conferencia_Misturas(self.app, self.mostrar_menu_conferencia)
        self.conteiner_frame = self.conferencia_misturas.frame
        self.conteiner_frame.pack(fill="both", expand=True)

    #conferencia sts
    def mostrar_conferencia_sts(self, event=None):
        self.limpar_tela()
        self.conferencia_sts = Conferencia_STS(self.app, self.mostrar_menu_conferencia)
        self.conteiner_frame = self.conferencia_sts.frame
        self.conteiner_frame.pack(fill="both", expand=True)
        
    #conferencia fines
    def mostrar_conferencia_fines(self, event=None):
        self.limpar_tela()
        self.conferencia_misturas = Conferencia_Fines(self.app, self.mostrar_menu_conferencia)
        self.conteiner_frame = self.conferencia_misturas.frame
        self.conteiner_frame.pack(fill="both", expand=True)

    def opt(self, event=None):
        
        opcao = self.rodape.entry_OPT.get().strip()

        if opcao == "1":
            self.rodape.entry_OPT.delete(0, "end")
            self.mostrar_conferencia_misturas()

        elif opcao =="2":
            self.rodape.entry_OPT.delete(0, "end")
            return
        
        else:
            self.rodape.entry_OPT.delete(0, "end")



    def voltar(self, evente=None):
        self.voltar()
