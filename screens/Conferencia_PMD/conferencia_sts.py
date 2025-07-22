import customtkinter as ctk
import datetime
from PIL import Image
import winsound
import re

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
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


class Conferencia_STS():
#construçao principal 
    def __init__(self, app, voltar):
        #configuracoes padrao do frame
        self.app = app
        self.frame = ctk.CTkFrame(self.app)
        self.item_atual = 0
        self.cont = 0
        self.codigos_confirmados = 1
        self.voltar = voltar
        #inicializacao de funcoes construtivas
        self.cabecalho()
        self.solcitacao_op()

    #cabecalho
    def cabecalho(self):
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
            text="CONFERENCIA STS", 
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

    #solicitação do op
    def solcitacao_op(self):
        self.frame_solicitacao_op = ctk.CTkFrame(self.frame)
        self.frame_solicitacao_op.pack(expand=True, fill=None, anchor="center")
        
        self.titulo_solicitacao_op = ctk.CTkLabel(self.frame_solicitacao_op, text="    Solicitação de OP", bg_color=config.CORES["texto"], text_color=config.CORES["fundo"], width=700, height=50, anchor="w", font=("Arial", 20))
        self.titulo_solicitacao_op.pack(side="top")

        self.mensagem_solicitacao_op = ctk.CTkLabel(self.frame_solicitacao_op, text="  Informe a OP que deseja conferir: ", anchor="w", justify="left", font=("Arial", 18))
        self.mensagem_solicitacao_op.pack(anchor="w", pady=(20 , 5))

        self.entry_solicitacao_op = ctk.CTkEntry(self.frame_solicitacao_op, placeholder_text="Ordem de Produção", height=40)
        self.entry_solicitacao_op.pack(fill="x", expand=True, padx=10)
        
        self.botao_voltar_solicitacao_op = ctk.CTkButton(self.frame_solicitacao_op, text="VOLTAR", height=50, width=100, font=("Arial", 15, "bold"), fg_color=config.CORES["texto"], text_color=config.CORES["fundo"])
        self.botao_voltar_solicitacao_op.pack(side="left", padx=10, pady=20)
        
        self.botao_continuar_solicitacao_op = ctk.CTkButton(self.frame_solicitacao_op, text="CONTINUAR", height=50, width=100, font=("Arial", 15, "bold"), fg_color=config.CORES["texto"], text_color=config.CORES["fundo"], command=self.conferir_STS)
        self.botao_continuar_solicitacao_op.pack(side="right", padx=10, pady=20)
        
        self.entry_solicitacao_op.bind("<Return>", command=self.conferir_STS)
        self.app.bind("<Escape>")
        func.focar_campo(self.frame, self.entry_solicitacao_op)


# ----------- Definiçoes Funcionais ---------
    def atualizar_relogio(self):
        agora = datetime.datetime.now().strftime("%H:%M:%S")
        self.label_relogio.configure(text=agora)
        self.frame.after(1000, self.atualizar_relogio)

    def conferir_STS(self, event=None):
        #obtem dado do entry
        self.entrada_op = self.entry_solicitacao_op.get().strip()

        #acha nome de arquivo
        self.nome_arquivo = op.achar_arquivo(self.entrada_op, "sts")

        #mensagem de erro caso não ache arquivo
        if self.nome_arquivo == "N/A" or self.entrada_op == "":
            self.erro_solicitacao_op = ctk.CTkLabel(self.frame_solicitacao_op, text="OP não encontrada na programação", bg_color=config.CORES["erro"], text_color=config.CORES["texto"], height=40, font=("Arial", 20, "bold"))
            self.erro_solicitacao_op.pack(padx=10, pady=20, side="bottom", fill="x", expand=True)
            self.frame.after(1500,self.erro_solicitacao_op.pack_forget)
            winsound.MessageBeep(winsound.MB_ICONHAND)
            return
        else:
            #obtem dataframe e slava quantos codigos exitem nela
            self.data_frame_completo = op.obter_sts(self.nome_arquivo)
            self.quantidade_total_de_codigos = len(self.data_frame_completo)
            
            #verifica em qual item estamos e qual a hora de parar
            if self.quantidade_total_de_codigos >= self.item_atual:
                self.verificar_item(self.item_atual)


    #verificar itme propriamente dito 
    def verificar_item(self, item_atual, event=None):
        item = self.data_frame_completo.loc[item_atual, "Material"]
        peso = self.data_frame_completo.loc[item_atual, "Quantity"]
        print(item, peso)
        self.lista = []
        self.lista = self.cirar_lista_item(item, peso)
        print("Lista criada com sucesso")
        self.total = len(self.lista)
        if self.lista: 
            self.cirar_criar_tela_conferencia()


    
    def cirar_criar_tela_conferencia(self):
        #otbtem df com dados
            
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
            self.label_confirmar = ctk.CTkLabel(self.frame_acofirmar, text=self.lista[self.cont], height=100, width=400, font=("Arial", 60, "bold"), text_color=config.CORES["texto"])
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
        if self.cont < len(self.lista):
            mistura  = self.lista[self.cont]
            self.label_confirmar.configure(text=mistura)
        else:
            print("codigos confirmados", self.quantidade_total_de_codigos, self.codigos_confirmados)
            if self.quantidade_total_de_codigos == self.codigos_confirmados:
                self.fim = ctk.CTkToplevel(self.app)
                self.fim.geometry("300x100")
                self.fim.title("FIM")
                self.botao_finalizar = ctk.CTkButton(self.fim, text="FINALIZAR", fg_color=config.CORES["texto"], text_color=config.CORES["fundo"], command=self.Voltar)
                self.botao_finalizar.pack()

                self.fim.lift()
                self.fim.focus_force()
                self.fim.grab_set()
            else:
                self.label_confirmar.configure(text="Fim da misturas")
                self.cont = 0
                self.item_atual += 1
                self.codigos_confirmados += 1
                self.frame_conteiner.pack_forget()
                self.verificar_item(self.item_atual)

    def verificar_mistura(self, event=None):
        if self.cont >= len(self.lista):
            return
        entrada = self.entry_aconfirmar.get().strip()
        mistura = self.lista[self.cont]
        self.entry_aconfirmar.delete(0, "end")
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
            print(f"Código {entrada} incoerente com {mistura}")

            self.messagem_erro = ctk.CTkLabel(self.frame_conteiner, text="CÓDIGO NÃO CONFERE", width=300, height=80, font=("Arial", 20, "bold"), fg_color=config.CORES["erro"])
            self.messagem_erro.grid(row=4, column=2, padx=10, pady=10)
            winsound.MessageBeep(winsound.MB_ICONHAND)


    def cirar_lista_item(self, item, peso):
        peso = int(peso)
        self.lista_resultado = []
        def criar_lista(event=None):
            try:
                peso_unitario = entry_solicitacao_peso.get().strip()
                peso_unitario = int(peso_unitario)

                if peso % peso_unitario == 0:
                    quantidade_codigo = peso / peso_unitario
                    quantidade_codigo = int(quantidade_codigo)
                    print(quantidade_codigo)
                    for i in range(0, quantidade_codigo):
                        self.lista_resultado.append(item)
                    print(self.lista_resultado)
                    app.destroy()

                else:
                    erro_solicitacao_op = ctk.CTkLabel(frame_solicitacao_peso, text="PESO INVALIDO", bg_color=config.CORES["erro"], text_color=config.CORES["texto"], height=40, font=("Arial", 20, "bold"))
                    erro_solicitacao_op.pack(padx=10, pady=20, side="bottom", fill="x", expand=True)
                    frame.after(1500,erro_solicitacao_op.pack_forget)
                    winsound.MessageBeep(winsound.MB_ICONHAND)

                entry_solicitacao_peso.delete(0, "end")
            except:
                erro_solicitacao_op = ctk.CTkLabel(frame_solicitacao_peso, text="PESO INVALIDO", bg_color=config.CORES["erro"], text_color=config.CORES["texto"], height=40, font=("Arial", 20, "bold"))
                erro_solicitacao_op.pack(padx=10, pady=20, side="bottom", fill="x", expand=True)
                frame.after(1500,erro_solicitacao_op.pack_forget)
                winsound.MessageBeep(winsound.MB_ICONHAND)
        app = ctk.CTkToplevel()
        app.geometry("650x230")
        app.title("Solicitação de peso unitário")
        frame = ctk.CTkFrame(app)
        frame.pack(fill="both", expand=True)

        frame_solicitacao_peso = ctk.CTkFrame(frame)
        frame_solicitacao_peso.pack(expand=True, fill=None, anchor="center")
        
        titulo_solicitacao_peso = ctk.CTkLabel(frame_solicitacao_peso, text="    Solicitação de Peso Unitário", bg_color=config.CORES["texto"], text_color=config.CORES["fundo"], width=700, height=50, anchor="w", font=("Arial", 20))
        titulo_solicitacao_peso.pack(side="top")

        mensagem_solicitacao_peso = ctk.CTkLabel(frame_solicitacao_peso, text=f"  Informe o peso unitário do código {item}: ", anchor="w", justify="left", font=("Arial", 18))
        mensagem_solicitacao_peso.pack(anchor="w", pady=(20 , 5))

        entry_solicitacao_peso = ctk.CTkEntry(frame_solicitacao_peso, placeholder_text="Ordem de Produção", height=40)
        entry_solicitacao_peso.pack(fill="x", expand=True, padx=10)
        
        botao_voltar_solicitacao_peso = ctk.CTkButton(frame_solicitacao_peso, text="VOLTAR", height=50, width=100, font=("Arial", 15, "bold"), fg_color=config.CORES["texto"], text_color=config.CORES["fundo"])
        botao_voltar_solicitacao_peso.pack(side="left", padx=10, pady=20)
        
        botao_continuar_solicitacao_peso = ctk.CTkButton(frame_solicitacao_peso, text="CONTINUAR", height=50, width=100, font=("Arial", 15, "bold"), fg_color=config.CORES["texto"], text_color=config.CORES["fundo"], command=criar_lista)
        botao_continuar_solicitacao_peso.pack(side="right", padx=10, pady=20)

        func.focar_campo(app, entry_solicitacao_peso)
        entry_solicitacao_peso.bind("<Return>", criar_lista)
        frame_solicitacao_peso.wait_window()

        print("Janela fechada")
        return self.lista_resultado

    def Voltar(self, event=None):
        self.voltar()
