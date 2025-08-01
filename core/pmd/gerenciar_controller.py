#controla tela de gerenciamento
#Criador: Marcus Vinicius Hilário de Oliveira
#Data: 30/07/2025


#------------------ inportações Externas --------------------
import customtkinter as ctk
#------------------ inportações Externas --------------------


#------------------ inportações internas --------------------
import config.colors as cor
import model.pmd.gerenciar_model as model
#------------------ inportações internas --------------------

class botao_indentificador(ctk.CTkFrame):
    def __init__(self,frame, id, op, qtd_confirm, status, total, tipo, comando):
        super().__init__(frame, fg_color=self.get_cor(status), height=40, width=800)

        self.pack_propagate(False)

        self.op = op
        self.id = id
        self.tipo = tipo
        self.status = status
        self.frame = frame
        self.atualizar = comando


        self.texto = ctk.CTkLabel(
            self, 
            text=f"   OP: {self.op}   ",
            fg_color="transparent",
            text_color=cor.DHL_COLORS["text_dark"],
            font=("Arial", 20, "bold"),
           

        )
        self.texto.pack(side="left", anchor="n", fill="both", expand=True)





        self.label_quantidade = ctk.CTkLabel(
            self, 
            height=40,
            text=f" {str(qtd_confirm)}/{str(total)}  ",
            font=("Arial", 20, "bold"),

        )
        self.label_quantidade.pack(side="left", padx=20)

        self.label_status = ctk.CTkLabel(
            self,
            height=40,
            text=(status.upper()),
            font=("Arial", 20, "bold"),
        )
        #self.label_status.pack(side="right", padx=20)



        self.botao_seletor = ctk.CTkOptionMenu(
            self,
            values=["pendente", "concluido", "cancelado"],
            command=self.executar_mudanca_de_satatus
            
        )
        self.botao_seletor.pack(side="right", padx=20)
        self.botao_seletor.set(status)


    def executar_mudanca_de_satatus(self, values):
        model.alterar_status(self.op, self.tipo, values, self.id)
        self.atualizar()
        print(values)

    

    def get_cor(self, status):
        
        if status == "pendente":
            return cor.DHL_COLORS["warning"]
        elif status == "concluido":
            return cor.DHL_COLORS["success"]
        elif status == "cancelado":
            return cor.DHL_COLORS["danger"]





    

def mostrar_mistura(tipo, frame, comando):

    lista_de_misturas = model.listar_mistura(tipo)
    if lista_de_misturas:
        print(lista_de_misturas)

        for item in lista_de_misturas:
            botao_indentificador(frame, item[0], item[1], item[2], item[3], item[4], tipo, comando).pack(pady=10)

