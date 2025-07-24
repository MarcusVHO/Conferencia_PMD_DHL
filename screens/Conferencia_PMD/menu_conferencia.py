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
        #cabeçalho 
        self.header = ctk.CTkFrame(
            self.frame,
            height=90,
            fg_color=config.CORES["primaria"],
            corner_radius=False)
        self.header.pack(side="top", fill="x")


        #Logo
        self.logo_image = ctk.CTkImage(Image.open(config.APP_ICO_PNG), size=(60,60))
        self.logo_label = ctk.CTkLabel(
            self.header, 
            image=self.logo_image, 
            text=""
            )
        self.logo_label.pack(side="left", padx=10)

        #Titulo
        self.titulo_label = ctk.CTkLabel(
            self.header, 
            text="Seleção de Conferencia", 
            font=("Arial",20), 
            text_color=config.CORES["texto"])
        self.titulo_label.pack(side="left", padx=10)
        
        #Espaço par Empurrar restante a direita
        self.espaco = ctk.CTkLabel(self.header, text="").pack(side="left", expand=True)

        #Relógio
        self.label_relogio = ctk.CTkLabel(
            self.header, 
            text="", 
            font=("Arial",20), 
            text_color="black")
        self.label_relogio.pack(side="right", padx=10)
        self.atualizar_relogio()

        #Data
        data_hoje = datetime.datetime.now().strftime("%d/%m/%Y")
        self.label_data = ctk.CTkLabel(
            self.header, 
            text=data_hoje, 
            font=("Arial",20),
            text_color=config.CORES["texto"])
        self.label_data.pack(side="right", padx=10)

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




        #Rodapé
        self.footer = ctk.CTkFrame(self.frame, height=70, fg_color=config.CORES["primaria"], corner_radius=False)
        self.footer.pack(side="bottom", fill="x", padx=20)

        #botão voltar
        self.botao_voltar = ctk.CTkButton(self.footer, height=40, width=100, text="VOLTAR", fg_color=config.CORES["texto"], text_color=config.CORES["fundo"], font=("Arial", 20, "normal"), command=voltar)
        self.botao_voltar.pack(side="left")

        #Entry rodapé
        self.entry_OPT = ctk.CTkEntry(self.footer,width=100)
        self.entry_OPT.pack(side="right" )

        #Texto entry
        self.label_OPT = ctk.CTkLabel(
            self.footer,
            text="OPT: ",
            font=("Arial",20)
        )
        self.label_OPT.pack(side="right", pady=20, padx=10)
        func.focar_campo(self.app, self.entry_OPT)
        #funcional
        self.entry_OPT.bind("<Return>", command=self.opt)
        self.app.bind("<Escape>", self.voltar)
          

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
        
        opcao = self.entry_OPT.get().strip()

        if opcao == "1":
            self.entry_OPT.delete(0, "end")
            self.ir_para_misturas_normais()

        elif opcao =="2":
            self.entry_OPT.delete(0, "end")
            return
        
        else:
            self.entry_OPT.delete(0, "end")



    def voltar(self, evente=None):
        self.voltar()
