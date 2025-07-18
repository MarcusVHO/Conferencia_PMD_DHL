import customtkinter as ctk
from PIL import Image
import datetime
import winsound
import sys
import os 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import config

class Menu_Conferencia():
    def __init__(self):
        self.app = None
        self.opcao = None
    
    def abrir(self):
        #inicialização do app
        self.app = ctk.CTk()
        self.app.title(config.APP_TITLE)
        self.app.geometry(config.APP_SIZE)
        self.app.iconbitmap(config.APP_ICO)
        ctk.set_appearance_mode(config.APP_THEME)
        self.app.configure(fg_color=config.CORES["primaria"])

        #cabeçalho 
        self.header = ctk.CTkFrame(
            self.app,
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
            self.app,
            height=100,
            fg_color=config.CORES["primaria"]
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
            command=lambda: self.enviar_informacao("1"),
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
            command=lambda: self.enviar_informacao("2"),
            corner_radius=0)
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
            command=lambda: self.enviar_informacao("3"),
            corner_radius=0)
        self.botao_conferir_fines_btn.pack(side="left",padx=(0,1), pady=1, fill="both", expand=True)
        #Rodapé
        self.footer = ctk.CTkFrame(self.app, height=70, fg_color=config.CORES["primaria"])
        self.footer.pack(side="bottom", fill="x")

        #Texto entry
        self.label_OPT = ctk.CTkLabel(
            self.footer,
            text="OPT: ",
            font=("Arial",20)
        )
        self.label_OPT.pack(side="left", pady=20)

        #Entry rodapé
        self.entry_OPT = ctk.CTkEntry(
            self.footer,
            width=100
        )
        self.entry_OPT.pack(side="left" )

        #funcional
        self.app.bind("<Return>", self.pegar_informação)
        

        self.app.mainloop()



    def pegar_informação(self, event=None):
        self.opcao = self.entry_OPT.get().strip()
        self.entry_OPT.delete(0, "end")

        if self.opcao in ["1", "2", "3"]:
            self.app.quit()
            self.fechar()
        else:
             winsound.MessageBeep(winsound.MB_ICONHAND)
             self.opcao = None

    def enviar_informacao(self,inform, event=None):
        self.opcao = inform
        self.app.quit()
        self.fechar()
       

    def atualizar_relogio(self):
        agora = datetime.datetime.now().strftime("%H:%M:%S")
        self.label_relogio.configure(text=agora)
        self.app.after(1000, self.atualizar_relogio)

    def fechar(self):
        self.app.destroy()


if __name__ == "__main__":
    menu_conferencia = Menu_Conferencia()
    menu_conferencia.abrir()
    print(menu_conferencia.opcao)