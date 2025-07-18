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
import winsound


class Tela_Inicial():
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
            text="Sistema de Conferência PMD", 
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
            text="CONFERÊNCIA", 
            height=90,
            width=190, 
            fg_color=config.CORES["fundo"], 
            hover_color=config.CORES["borda"],
            font=("Arial", 20),
            text_color=config.CORES["texto"],
            command=lambda: self.enviar_informacao("conferencia"),
            corner_radius=0)
        self.botao_conferencia_btn.pack(fill="both", expand=True)

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
            text_color=config.CORES["texto"],
            command=lambda: self.enviar_informacao("relatorio"),
            )
        self.botao_relatório_btn.pack(fill="both", expand=True)

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

        #Funcional
        self.app.bind("<Return>", self.pegar_informação)
        
        self.app.mainloop()



    def atualizar_relogio(self):
        agora = datetime.datetime.now().strftime("%H:%M:%S")
        self.label_relogio.configure(text=agora)
        self.app.after(1000, self.atualizar_relogio)

    def pegar_informação(self, event=None):
        self.opcao = self.entry_OPT.get().strip()
        self.entry_OPT.delete(0, "end")

        if self.opcao in ["conferencia", "relatorio"]:
            self.app.quit()
            self.fechar() 
        else:
            winsound.MessageBeep(winsound.MB_ICONHAND)

    def enviar_informacao(self,inform, event=None):
        self.opcao = inform
        self.app.quit()
        self.fechar() 

    def fechar(self):
        self.app.destroy()

if __name__ == '__main__':
    tela_inicial = Tela_Inicial()
    tela_inicial.abrir()
    print(tela_inicial.opcao)