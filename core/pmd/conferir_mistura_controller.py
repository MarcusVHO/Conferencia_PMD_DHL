#Responsavel por controlar conferencia de misturas normais
#Criador: Marcus Vinicius Hilário de Oliveira
#Data: 28/07/2025

#------------------ Importacoes Externas ----------------------
import json
import customtkinter as ctk
import re
#------------------ Importacoes Externas ----------------------



#------------------ Importacoes Internas ----------------------
import model.pmd.conferir_mistura_model as model
import config.colors as cor
#------------------ Importacoes Internas ----------------------

class label_confirmados():
    def __init__(self, frame, mistura):
        self.label = ctk.CTkLabel(
            frame, 
            height=40,
            text= mistura,
            font=("Arial", 20, "bold"),
            text_color=cor.DHL_COLORS["text_dark"],
            fg_color=cor.DHL_COLORS["gray_medium"],
            corner_radius=20
        )

        children = frame.winfo_children()
        if children:  # Se já existe algum widget no frame
            if children[0].winfo_manager() == "pack":  # Garante que já foi empacotado
                self.label.pack(side="top", padx=10, pady=2, fill="x", expand=True, before=children[0])
            else:
                self.label.pack(side="top", padx=10, pady=2, fill="x", expand=True)
        else:
            self.label.pack(side="top", padx=10, pady=2, fill="x", expand=True)


def atualizar_dados(op, cont, type):

    dados = model.pegar_dados_uteis(op, type=type)
    dados = {
        "misturas": json.loads(dados[0]),
        "confirmados": dados[1],
        "status": dados[2],
        "total": dados[3]
    }
    
    if dados["confirmados"] == dados["total"]:
        print("CONFERENCIA TERMINOU")
        model.concluir(op, type)

        
    print(dados)
    return dados
    

#confere a mistura
def conferir_mistura(op, mistura_atual, texto_digitado, confirmados, type, frame):
    if mistura_atual in texto_digitado:
        confirmados += 1
        confirmado_lista = label_confirmados(frame, mistura_atual)
        model.atualizar_dado(op, confirmados, type=type)
        return True
    
    else:
        return False
    
#verifica de forma basica motivo do erro
def conferir_divergencia(op,confirmados, texto_digitado, misturas, frame_conteiner):
    
    parte = misturas[confirmados:]
    resultado = re.search(r"1.*[A-Za-z]$", texto_digitado)

    if resultado:
        texto_filtrado = resultado.group()

        if texto_filtrado in parte:
            encontrado = True
        else:
            encontrado = False
    

        if encontrado == True:
            print(f"CODIGO: {texto_digitado} FORA DA ORDEM")

            #cira mensagem de erro na tela
            label_erro = ctk.CTkLabel(
                frame_conteiner, 
                height=90, 
                fg_color=cor.DHL_COLORS["warning"],
                text=f"   CODIGO: {texto_digitado} FORA DA ORDEM   ", 
                font=("Arial", 30, "bold")
            )
            label_erro.grid(row= 3, column=2)
            label_erro.after(2000, label_erro.grid_forget)

        elif encontrado == False:
            print(f"ITEM {texto_digitado} NÂO ENCONTRADO EM {op}")
            
            #cira mensagem de erro na tela
            label_erro = ctk.CTkLabel(
                frame_conteiner, 
                height=90, 
                fg_color=cor.DHL_COLORS["warning"],
                text=f"   ITEM {texto_digitado} NÂO ENCONTRADO EM {op}   ", 
                font=("Arial", 30, "bold")
            )
            label_erro.grid(row= 3, column=2)
            label_erro.after(2000, label_erro.grid_forget)

    
