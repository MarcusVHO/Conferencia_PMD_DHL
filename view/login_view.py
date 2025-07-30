#Tela respnsavel por realizar coleta e interagir com o usuario para realizar o login
#Criador: Marcus Vinicius Hilário de Oliveira
#Data: 25/07/2025

#------------------ inportações Externas --------------------
import customtkinter as ctk
from PIL import Image
#------------------ inportações Externas --------------------

#------------------ inportações internas --------------------
import config.settings as st
import config.colors as cor
import core.login_controller as controler
import view.components.widgets_reutilizaveis as alerts
from view.components.screen_components import *
#------------------ inportações internas --------------------


#------------------- Classe Primária ---------------
class Login(ctk.CTkFrame):
    def __init__(self, master, navigate_to_home=None):
        #inicializacao primaria
        super().__init__(master)
        self.frame = ctk.CTkFrame(self, fg_color=cor.DHL_COLORS["primary"])
        self.frame.pack(fill="both", expand=True)
        
        #inicializacao de variaveis
        self.navigate_to_home = navigate_to_home
        
        #inicializacao de imagens
        person = ctk.CTkImage(light_image=Image.open(st.APP_IMG_PESSOA), size=(50,50))


        #inicializacao do cabecalho
        cabecalho = Cabecalho(self.frame, "LOGIN")

        #conteiner do login
        self.conteiner_login = ctk.CTkFrame(
            self.frame, 
            fg_color=cor.DHL_COLORS["gray_medium"],
            width=590,
            height=505,
            border_width=5
        )
        self.conteiner_login.pack(anchor="center", expand=True)

        #configuracao do frame conteiner
        self.conteiner_login.rowconfigure(0, weight=0)
        self.conteiner_login.rowconfigure(1, weight=1)
        self.conteiner_login.rowconfigure(2, weight=1)
        self.conteiner_login.rowconfigure(3, weight=1)
        self.conteiner_login.columnconfigure(0, weight=1)
        self.conteiner_login.columnconfigure(1, weight=1)
        self.conteiner_login.grid_propagate(False)

        
        #frame titulo do login
        titulo_login_frame = ctk.CTkFrame(
            self.conteiner_login,
            height=70,
            fg_color=cor.DHL_COLORS["gray_dark"]
        )
        titulo_login_frame.grid(row=0, column=0, columnspan=2, sticky="we")
        titulo_login_frame.pack_propagate(False)

        #imagem pesso
        person_img_label = ctk.CTkLabel(
            titulo_login_frame,
            image=person,
            text=""
        )
        person_img_label.pack(side="left", anchor="center", padx=20)

        #label titulo login
        titulo_login_label = ctk.CTkLabel(
            titulo_login_frame,
            text="LOGIN",
            font=("Arial", 30, "bold"),
            text_color=cor.DHL_COLORS["text_light"]
        )
        titulo_login_label.pack(side="left", anchor="center", padx=10)



        #campo usuario
        usuario_label = ctk.CTkLabel(
            self.conteiner_login,
            text="USUARIO: ",
            font=("Arial",40,"bold")
        )
        usuario_label.grid(row=1, column=0, stick="e")

        self.usuario_entry = ctk.CTkEntry(
            self.conteiner_login, 
            height=40, 
            placeholder_text="USUARIO"
        )
        self.usuario_entry.grid(row=1, column=1, sticky="we", padx=20)
        self.frame.after(100, lambda: self.usuario_entry.focus())
        self.usuario_entry.bind("<Return>", self.trocar_campo)


        #campo senha
        senha_label = ctk.CTkLabel(
            self.conteiner_login,
            text="SENHA: ",
            font=("Arial",40,"bold")
        )
        senha_label.grid(row=2, column=0, stick="e")

        self.senha_entry = ctk.CTkEntry(
            self.conteiner_login,
            show="*",
            height=40, 
            placeholder_text="SENHA",
            
        )
        self.senha_entry.grid(row=2, column=1, sticky="we", padx=20)
        self.senha_entry.bind("<Return>", self.logar)
        

        #botao entrar
        self.botao_entrar = ctk.CTkButton(
            self.conteiner_login,
            height=70,
            text="ENTRAR",
            font=("Arial", 20, "bold"),
            fg_color=cor.DHL_COLORS["black"],
            text_color=cor.DHL_COLORS["text_light"],
            command=self.logar
        )
        self.botao_entrar.grid(row=3, column=1, sticky="we", padx=20)

        

#------------------- Classe Primária ---------------

#------------------- Fucoes subordinadas --------------
    #troca de campo ao dar enter
    def trocar_campo(self, event=None):
        self.senha_entry.focus()

    #comunica com core para validar login
    def logar(self, event=None):
        usuario_digitado = self.usuario_entry.get().strip()
        senha = self.senha_entry.get().strip()
        #usuario_digitado = "85197893"
        #senha = "088727"

        resposta, mensagem = controler.validar_login(usuario_digitado, senha)

        print(f"Logado como: {mensagem}")
        if resposta == True:
            self.navigate_to_home()

        elif resposta == False:
            alerts.box_alert_universal(self.frame, "erro", "Usuario ou Senha invalidos").pack(pady=20)
            self.usuario_entry.delete(0, "end")
            self.senha_entry.delete(0, "end")
            self.usuario_entry.focus()


