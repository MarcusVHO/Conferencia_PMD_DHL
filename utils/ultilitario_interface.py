import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import config
from PIL import Image
import customtkinter as ctk
import datetime
import utils.funcoes as func


class Cabecalho():

    def __init__(self, frame_pai, titulo):
        #inicialização de variaveis
        self.frame = frame_pai

         #cabeçalho 
        self.header = ctk.CTkFrame(
            self.frame,
            height=90,
            fg_color=config.CORES["primaria"])
        
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
            text=titulo, 
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

        #USUARIO
        if config.USUARIO_LOGADO == None:
            pass
        else:
            label_usuario = ctk.CTkLabel(
                self.header, 
                text=config.USUARIO_LOGADO["nomeusuario"],
                text_color=config.CORES["texto"],
                font=("Arial",30, "bold"),
                
            )
            label_usuario.pack(side="right", padx=100)




    def atualizar_relogio(self):
        agora = datetime.datetime.now().strftime("%H:%M:%S")
        self.label_relogio.configure(text=agora)
        self.frame.after(1000, self.atualizar_relogio)


class Rodape():
    def __init__(self, frame_pai, voltar, command):
        #inicialização de variaveis
        self.frame = frame_pai

         #Rodapé
        self.footer = ctk.CTkFrame(self.frame, height=70, fg_color=config.CORES["primaria"], corner_radius=False)
        self.footer.pack(side="bottom", fill="x")

        #Entry rodapé
        self.entry_OPT = ctk.CTkEntry(
            self.footer,
            width=100
        )
        self.entry_OPT.pack(side="right", padx=(0,30))
        func.focar_campo(self.frame, self.entry_OPT)

        #Texto entry
        self.label_OPT = ctk.CTkLabel(
            self.footer,
            text="OPT: ",
            font=("Arial",20)
        )
        self.label_OPT.pack(side="right", pady=20)


        if voltar == True:
            botao_voltar = ctk.CTkButton(
                self.footer,
                text="VOLTAR",
                height=50,
                width=200,
                fg_color=config.CORES["fundo_dark"],
                text_color=config.CORES["texto_dark"],
                command=command,
            )
            botao_voltar.pack(side="left", padx=10)
        #Funcional


    def atualizar_relogio(self):
        agora = datetime.datetime.now().strftime("%H:%M:%S")
        self.label_relogio.configure(text=agora)
        self.frame.after(1000, self.atualizar_relogio)
