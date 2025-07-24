import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import customtkinter as ctk
import utils.funcoes as func
import utils.ultilitario_interface as interface
import config
from PIL import Image
import DB.usuarios_database as dbuser


#Tela responsavel por login de usuarios
class Login():
    def __init__(self, app, irparatelainicial):

        #inicialização de variaveis
        self.app = app
        self.frame = ctk.CTkFrame(
            self.app, 
            fg_color=config.CORES["primaria"],
            corner_radius=False,
        )
        self.ir_para_tela_inicial = irparatelainicial

        #inicialziação de cabecalho
        cabecalho = interface.Cabecalho(self.frame, "LOGIN")


        #frame conteiner login
        frame_login = ctk.CTkFrame(
            self.frame, 
            width=620, 
            height=470,
            border_color=config.CORES["borda_dark"],
            border_width=2,
            corner_radius=False,
        )
        frame_login.grid_rowconfigure(0, weight=0)
        frame_login.grid_rowconfigure(1, weight=0)
        frame_login.grid_rowconfigure(2, weight=0)
        frame_login.grid_rowconfigure(3, weight=0)
        frame_login.grid_columnconfigure(0, weight=0)
        frame_login.grid_columnconfigure(1, weight=10)
        frame_login.pack(pady=20, anchor="center", expand=True)
        frame_login.grid_propagate(False)


        #frame titulo
        frame_titulo_login = ctk.CTkFrame(
            frame_login, 
            height=70,
            fg_color=config.CORES["fundo_dark"],
            corner_radius=False,
        )
        frame_titulo_login.grid(row=0, column=0, columnspan=2, sticky="ew")


        #cirar imagem para frame titulo
        imagem_pessoa = ctk.CTkImage(light_image=Image.open(config.APP_IMG_PESSOA), size=(100,100))
        label_imagem_pessoa = ctk.CTkLabel(frame_titulo_login, image=imagem_pessoa, text=" ")
        label_imagem_pessoa.pack(side="left", padx=10)

        #texto titulo frame login
        titulo_login = ctk.CTkLabel(frame_titulo_login, text="LOGIN", text_color=config.CORES["texto_dark"], font=("Arial", 40, "bold"))
        titulo_login.pack(side="left", padx=10)

        #titulo usuario
        label_usuario = ctk.CTkLabel(frame_login, text="USUARIO: ", font=("Arial", 30, "bold"))
        label_usuario.grid(row=1, column=0, pady=(50,50), padx=20)
        
        #entry usuario
        self.entry_usuario = ctk.CTkEntry(frame_login, placeholder_text="USUARIO", height=40)
        self.entry_usuario.grid(row=1, column=1, sticky="ew", padx=30, pady=(50,50))

        #titulo usuario
        self.label_senha = ctk.CTkLabel(frame_login, text="SENHA: ", font=("Arial", 30, "bold"))
        self.label_senha.grid(row=2, column=0, padx=20, pady=(50,50))

        #entry senha
        self.entry_senha = ctk.CTkEntry(frame_login, placeholder_text="SENHA", height=40, show="*")
        self.entry_senha.grid(row=2, column=1, sticky="ew", padx=30, pady=(50,50))

        #botão entrar
        botao_entrar = ctk.CTkButton(frame_login, text="ENTRAR", fg_color=config.CORES["fundo_dark"], text_color=config.CORES["texto_dark"], height=70, command=self.logar)
        botao_entrar.grid(row=4, column=0, columnspan=2, sticky="ew", padx=30, )

        #ultilitario dos campos
        func.focar_campo(self.frame, self.entry_usuario)
        self.entry_usuario.bind("<Return>", self.focar_proximo_campo)
        self.entry_senha.bind("<Return>", self.logar)



    def logar(self, event=None):
        """RESPONSAVEL PELO LOGIN NO SISTEMA"""
        idusuario_digitado = self.entry_usuario.get().strip()
        senha_digitada = self.entry_senha.get().strip()
        resultado = dbuser.logar(idusuario_digitado, senha_digitada)
        config.USUARIO_LOGADO = resultado
        print(resultado)

        if resultado:
            print(f"Usuario: {resultado["nomeusuario"]} conectado")
            self.ir_para_tela_inicial()

        elif resultado == False:
            config.USUARIO_LOGADO = None
            
            popup_usuario_incorreto = ctk.CTkLabel(
                self.frame,
                text="  USUARIO OU SENHA INCORRETO  ",
                height=70,
                fg_color=config.CORES["secundaria"],
                font=("Arial", 30, "bold")
            )
            popup_usuario_incorreto.pack(padx=20, pady=20)
            self.frame.after(1500, popup_usuario_incorreto.pack_forget)
        
        else:
            print("ERRO NO LOGIN")

    def focar_proximo_campo(self, event=None):
        self.entry_senha.focus()
    
