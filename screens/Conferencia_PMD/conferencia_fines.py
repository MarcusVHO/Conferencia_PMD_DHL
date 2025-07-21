import customtkinter as ctk
import datetime
from PIL import Image
import winsound
import re

import sys
import os 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import config
import utils.funcoes as func
import utils.operacoes as op

class Confirmado():
            def __init__(self,frame, codigo, cor):
                    super().__init__()
                    self.codigo = codigo
                    self.cor = cor
                    self.frame_lista_direita = frame
                    self.inserir()
            def inserir(self):
                    self.codigo_confirmado = ctk.CTkLabel(self.frame_lista_direita, text=self.codigo, fg_color=config.CORES["borda"], height=40, corner_radius=20, font=("Arial", 18, "bold"))
                    self.codigo_confirmado.pack(fill="x", padx=5, pady=5)

                    self.frame_lista_direita.after(10, self.rolar_pra_baixo)
            def rolar_pra_baixo(self):
                 self.frame_lista_direita._parent_canvas.yview_moveto(1.0)

class Conferencia_Fines():
    def __init__(self, app, voltar):
        self.app = app
        self.frame = ctk.CTkFrame(self.app)
        self.cont = 0
        self.total = 0
        self.voltar = voltar

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
            text="CONFERENCIA FINES", 
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


        #Solicitação de OP
        self.frame_solicitacao_op = ctk.CTkFrame(self.frame)
        self.frame_solicitacao_op.pack(expand=True, fill=None, anchor="center")
        
        self.titulo_solicitacao_op = ctk.CTkLabel(self.frame_solicitacao_op, text="    Solicitação de OP", bg_color=config.CORES["texto"], text_color=config.CORES["fundo"], width=700, height=50, anchor="w", font=("Arial", 20))
        self.titulo_solicitacao_op.pack(side="top")

        self.mensagem_solicitacao_op = ctk.CTkLabel(self.frame_solicitacao_op, text="  Informe a OP que deseja conferir: ", anchor="w", justify="left", font=("Arial", 18))
        self.mensagem_solicitacao_op.pack(anchor="w", pady=(20 , 5))

        self.entry_solicitacao_op = ctk.CTkEntry(self.frame_solicitacao_op, placeholder_text="Ordem de Produção", height=40)
        self.entry_solicitacao_op.pack(fill="x", expand=True, padx=10)
        
        self.botao_voltar_solicitacao_op = ctk.CTkButton(self.frame_solicitacao_op, text="VOLTAR", height=50, width=100, font=("Arial", 15, "bold"), fg_color=config.CORES["texto"], text_color=config.CORES["fundo"], command=self.voltar)
        self.botao_voltar_solicitacao_op.pack(side="left", padx=10, pady=20)
        
        self.botao_continuar_solicitacao_op = ctk.CTkButton(self.frame_solicitacao_op, text="CONTINUAR", height=50, width=100, font=("Arial", 15, "bold"), fg_color=config.CORES["texto"], text_color=config.CORES["fundo"], command=self.conferir_fines)
        self.botao_continuar_solicitacao_op.pack(side="right", padx=10, pady=20)
        
        self.entry_solicitacao_op.bind("<Return>", command=self.conferir_fines)
        self.app.bind("<Escape>", self.voltar)
        func.focar_campo(self.frame, self.entry_solicitacao_op)

        


    def conferir_fines(self, event=None):
        self.entrada_op = self.entry_solicitacao_op.get().strip()

        #acha nome de arquivo
        self.nome_arquivo = op.achar_arquivo(self.entrada_op)

        

        if self.nome_arquivo == "N/A" or self.entrada_op == "":
            self.erro_solicitacao_op = ctk.CTkLabel(self.frame_solicitacao_op, text="OP não encontrada na programação", bg_color=config.CORES["erro"], text_color=config.CORES["texto"], height=40, font=("Arial", 20, "bold"))
            self.erro_solicitacao_op.pack(padx=10, pady=20, side="bottom", fill="x", expand=True)
            self.frame.after(1500,self.erro_solicitacao_op.pack_forget)
            winsound.MessageBeep(winsound.MB_ICONHAND)
            return

        else:
            #otbtem df com dados
            self.material = op.obter_fines(self.nome_arquivo)
            self.total = len(self.material)
            
            #Fecha frame de solicitação 
            self.frame_solicitacao_op.pack_forget()

            #cria novo frame para conferir
            self.frame_conteiner = ctk.CTkFrame(self.frame, fg_color=config.CORES["primaria"])
            self.frame_conteiner.pack(fill="both", expand=True) 

            #CONFIGS DO FRAME
            self.frame_conteiner.grid_rowconfigure(0, weight=1)   
            self.frame_conteiner.grid_rowconfigure(1, weight=1)  
            self.frame_conteiner.grid_rowconfigure(2, weight=1)   
            self.frame_conteiner.grid_rowconfigure(3, weight=1)   
            self.frame_conteiner.grid_rowconfigure(4, weight=1)   

            self.frame_conteiner.grid_columnconfigure(0, weight=0)  
            self.frame_conteiner.grid_columnconfigure(1, weight=1)
            self.frame_conteiner.grid_columnconfigure(2, weight=1) 
            self.frame_conteiner.grid_columnconfigure(3, weight=1) 
            self.frame_conteiner.grid_columnconfigure(4, weight=1) 

            # --------------- Frame Esquerdo ----------------------
            #cria caixa com infomacao da op
            self.frame_informacoes_mistura = ctk.CTkFrame(self.frame_conteiner, border_color=config.CORES["texto"], border_width=2, corner_radius=False, fg_color=config.CORES["fundo"])
            self.frame_informacoes_mistura.grid(row=0, column=0, rowspan=4, sticky="wn", padx=5, pady=5)

            #Titulo Informações Mistura
            self.label_titulo_informacoes_mistura = ctk.CTkLabel(self.frame_informacoes_mistura, text="MISTURA", font=("Arial", 20, "bold"), height=40, text_color=config.CORES["fundo"], fg_color=config.CORES["texto"])
            self.label_titulo_informacoes_mistura.pack(fill="x")
            
            #op dentro da caixa de informação
            self.label_op_caixa = ctk.CTkLabel(self.frame_informacoes_mistura, text=f"OP: {self.entrada_op}", height=70, width=300, font=("Arial",30,"bold"), text_color=config.CORES["texto"])
            self.label_op_caixa.pack(pady=10, padx=10)

            #Titulo Informações Quantidade
            self.label_titulo_informacoes_quantidade = ctk.CTkLabel(self.frame_informacoes_mistura, text="ITENS CONFIRMADOS", font=("Arial", 20, "bold"), height=40, text_color=config.CORES["fundo"], fg_color=config.CORES["texto"])
            self.label_titulo_informacoes_quantidade.pack(fill="x")

            #quantidade total confirmada
            self.label_quantidade_mistura = ctk.CTkLabel(self.frame_informacoes_mistura, text=f"{self.cont}/{self.total}", height=70, width=300, font=("Arial",30,"bold"), text_color=config.CORES["texto"])
            self.label_quantidade_mistura.pack(pady=10, padx=10)

            #Titulo Informações barra de progreco
            self.label_titulo_informacoes_progresso = ctk.CTkLabel(self.frame_informacoes_mistura, text="PROGRESSO", font=("Arial", 20, "bold"), height=40, text_color=config.CORES["fundo"], fg_color=config.CORES["texto"])
            self.label_titulo_informacoes_progresso.pack(fill="x")

            #barra de progresso
            self.barra_progresso_informacoes = ctk.CTkProgressBar(self.frame_informacoes_mistura, orientation="horizontal", height=20, progress_color=config.CORES["secundaria"], mode="determinate")
            self.barra_progresso_informacoes.pack(fill="x", pady=10, padx=5)
            self.barra_progresso_informacoes.set(0)

            # ---------------- Frame do Centro --------------------
            #a confirmar frame
            self.frame_acofirmar = ctk.CTkFrame(self.frame_conteiner, border_color=config.CORES["texto"], border_width=2, fg_color=config.CORES["borda"])
            self.frame_acofirmar.grid(row=1, column=2, padx=5, pady=(0, 5), sticky="n")

            self.frame_acofirmar.grid_rowconfigure(0, weight=1)
            self.frame_acofirmar.grid_rowconfigure(1, weight=1)
            self.frame_acofirmar.grid_rowconfigure(2, weight=1)

            #texto titulo frame a confirmar
            self.label_titulo_frame_aconfirmar = ctk.CTkLabel(self.frame_acofirmar, text="DHL - Misturas", height=100, font=("Arial", 50, "bold"), text_color=config.CORES["fundo"],fg_color=config.CORES["texto"])
            self.label_titulo_frame_aconfirmar.pack( padx=1, pady=1, fill="x")

            #a confirmar label texto
            self.label_confirmar = ctk.CTkLabel(self.frame_acofirmar, text=self.material[self.cont], height=100, width=400, font=("Arial", 60, "bold"), text_color=config.CORES["texto"])
            self.label_confirmar.pack(padx=5, pady=5, fill="x")

            #a confirmar entry 
            self.entry_aconfirmar = ctk.CTkEntry(self.frame_acofirmar, height=70, font=("Arial", 30))
            self.entry_aconfirmar.pack(padx=15, pady=(5, 15), fill="x")

            func.focar_campo(self.frame, self.entry_aconfirmar)

            self.entry_aconfirmar.bind("<Return>", lambda event: self.verificar_mistura())



            # --------------- Frame Direito ---------------------
            #frame lista historico
            self.frame_lista_direita = ctk.CTkScrollableFrame(
                 self.frame_conteiner, width=200, 
                 height=500, 
                 corner_radius=False, 
                 border_width=2, 
                 border_color=config.CORES["texto"], 
                 label_text="CONFIRMADOS", 
                 label_font=("Arial", 20, "bold"), 
                 label_fg_color=config.CORES["texto"],
                 label_text_color=config.CORES["fundo"]
                 )
            self.frame_lista_direita.grid(row=0, column=4, rowspan=3, padx=5, pady=1)


                


    def mostrar_mistura_atual(self):
        if self.cont < len(self.material):
            mistura  = self.material[self.cont]
            self.label_confirmar.configure(text=mistura)
        else:
            self.label_confirmar.configure(text=f"Fim dos FINES")
            self.entry_aconfirmar.configure(state="disabled")

    def verificar_mistura(self, event=None):
        if self.cont >= len(self.material):
            return
        entrada = self.entry_aconfirmar.get().strip()
        mistura = self.material[self.cont]
        
        if mistura in entrada:
            print("confirmada")

            #adiciona ultma confirmacao ao historico
            confirmado = Confirmado(self.frame_lista_direita, mistura, config.CORES["borda"],)

            
            #atualiza contador
            self.cont += 1

            #atualiza mistura na tela
            self.mostrar_mistura_atual()

            #atualiza texto de quantidade
            self.label_quantidade_mistura.configure(text=f"{self.cont}/{self.total}")

            #atualiza barra de progresso
            self.escala = self.cont/self.total
            if self.escala <= 0.25:
                 self.barra_progresso_informacoes.configure(progress_color="#DC3545")
            elif self.escala <= 0.5:
                 self.barra_progresso_informacoes.configure(progress_color="#cfa530")
            elif self.escala <= 0.75:
                 self.barra_progresso_informacoes.configure(progress_color="#2b51ce")
            elif self.escala <= 1:
                 self.barra_progresso_informacoes.configure(progress_color="#28a745")
                 
                
                 
            

            self.barra_progresso_informacoes.set(self.escala)

            self.messagem_sucesso = ctk.CTkLabel(self.frame_conteiner, text="CÓDIGO CONFIRMADA", width=300, height=80, font=("Arial", 20, "bold"), fg_color=config.CORES["sucesso"])
            self.messagem_sucesso.grid(row=4, column=2, padx=10, pady=10)
            winsound.MessageBeep(winsound.MB_OK)


        else:
            print("Mistura errada")
            print(self.cont)

            self.messagem_erro = ctk.CTkLabel(self.frame_conteiner, text="CÓDIGO NÃO CONFERE", width=300, height=80, font=("Arial", 20, "bold"), fg_color=config.CORES["erro"])
            self.messagem_erro.grid(row=4, column=2, padx=10, pady=10)
            winsound.MessageBeep(winsound.MB_ICONHAND)

        self.entry_aconfirmar.delete(0, "end")

    def atualizar_relogio(self):
        agora = datetime.datetime.now().strftime("%H:%M:%S")
        self.label_relogio.configure(text=agora)
        self.frame.after(1000, self.atualizar_relogio)

    def voltar(self):
        self.voltar()
    

if __name__ == "__main__":
        app = ctk.CTk()
        app.title(config.APP_TITLE)
        app.geometry(config.APP_SIZE)
        app.iconbitmap(config.APP_ICO)
        frame = None

        conferir = Conferencia_Misturas(app)
        frame = conferir.frame
        frame.pack(fill="both", expand=True)
        app.mainloop()