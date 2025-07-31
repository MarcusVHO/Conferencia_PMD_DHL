#intens que tendem a se reutilizar entre telas
#Criador: Marcus Vinicius Hilário de Oliveira
#Data: 25/07/2025


#------------------ inportações Externas --------------------
import customtkinter as ctk
from PIL import Image
import datetime
#------------------ inportações Externas --------------------

#------------------ inportações internas --------------------
import config.settings as st
import config.colors as cor
#------------------ inportações internas --------------------


#----------------------- Cabecalho  -------------------------

class Cabecalho():
    def __init__(self, frame_pai, titulo):
        #inicialização de variaveis
        self.frame = frame_pai

         #cabeçalho 
        self.header = ctk.CTkFrame(
            self.frame,
            height=90,
            fg_color=cor.DHL_COLORS["darklight"])
        
        self.header.pack(side="top", fill="x")


        #Logo
        self.logo_image = ctk.CTkImage(Image.open(st.APP_ICO_PNG), size=(60,60))
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
            font=("Arial",20,"bold"), 
            text_color=cor.DHL_COLORS["text_dark"])
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
            text_color=cor.DHL_COLORS["text_dark"])
        self.label_data.pack(side="right", padx=10)

        #USUARIO
        if st.USUARIO_LOGADO == None:
            pass
        else:
            label_usuario = ctk.CTkLabel(
                self.header, 
                text=st.USUARIO_LOGADO["nomeusuario"],
                text_color=cor.DHL_COLORS["text_dark"],
                font=("Arial",30, "bold"),
                
            )
            label_usuario.pack(side="right", padx=100)




    def atualizar_relogio(self):
        agora = datetime.datetime.now().strftime("%H:%M:%S")
        self.label_relogio.configure(text=agora)
        self.frame.after(1000, self.atualizar_relogio)

#----------------------- Cabecalho  -------------------------





#----------------------- Rodapé  ----------------------------

class Rodape():
    def __init__(self, frame_pai, voltar, command):
        #inicialização de variaveis
        self.frame = frame_pai

         #Rodapé
        self.footer = ctk.CTkFrame(self.frame, height=70, fg_color=cor.DHL_COLORS["darklight"], corner_radius=False)
        self.footer.pack(side="bottom", fill="x")
        self.footer.pack_propagate(False)




        #Entry rodapé
        self.entry_OPT = ctk.CTkEntry(
            self.footer,
            width=100
        )
        self.entry_OPT.pack(side="right", padx=(0,30))
        self.entry_OPT.focus()

        #Texto entry
        self.label_OPT = ctk.CTkLabel(
            self.footer,
            text="OPT: ",
            font=("Arial",20),
            text_color=cor.DHL_COLORS["text_dark"]
        )
        self.label_OPT.pack(side="right", pady=20)

        iform_criador = ctk.CTkLabel(self.footer, text="   Criador: Marcus Vinícius Hilário de Oliveira \nData: 21/07/2025                                         ", font=("Arial", 10,"bold"))
        iform_criador.pack(side="right",anchor="center", padx=50)

        if voltar == True:
            self.botao_voltar = ctk.CTkButton(
                self.footer,
                text="VOLTAR",
                height=50,
                width=200,
                fg_color=cor.DHL_COLORS["black"],
                text_color=cor.DHL_COLORS["text_light"],
                command=command,
            )
            self.botao_voltar.pack(side="left", padx=10)
#----------------------- Rodapé  ----------------------------





#-------------- cirar botoes automatico ---------------------
class botao():
    def __init__(self, master, Imagem, texto, command):
        self.frame_button = ctk.CTkFrame(master)
        

        self.frame_image = ctk.CTkFrame(
            self.frame_button, 
            fg_color=cor.DHL_COLORS["gray_dark"]
        )
        self.frame_image.pack(side="left")
        self.imagem = ctk.CTkLabel(
            self.frame_image, 
            image=Imagem, 
            text=" "
        )
        self.imagem.pack(anchor="center")

        self.texto = ctk.CTkButton(
            self.frame_button, 
            height=70, 
            text=texto, 
            font=("Arial", 30, "bold"),
            fg_color="transparent",
            text_color=cor.DHL_COLORS["text_dark"],
            width=200,
            hover_color=cor.DHL_COLORS["gray_dark"],
            command=command
        )
        self.texto.pack(anchor="center",fill="both", expand=True, padx=0,)

#-------------- cirar botoes automatico ---------------------

