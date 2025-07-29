#widgets reutilizaveis
#Criador: Marcus Vinicius Hilário de Oliveira
#Data: 25/07/2025

#------------------ inportações Externas --------------------
import customtkinter as ctk
#------------------ inportações Externas --------------------


#------------------ inportações internas --------------------
import config.colors as cor
#------------------ inportações internas --------------------


def box_alert_universal(app, type, message):
    if type == "erro":
        frame = ctk.CTkFrame(app, height=100, width=480, fg_color=cor.DHL_COLORS["danger"])
        frame.pack_propagate(False)
        
        label = ctk.CTkLabel(frame, text=f"  {message}  ", font=("Arial", 30, "bold"), text_color=cor.DHL_COLORS["text_dark"])
        label.pack(anchor="center", fill="x", expand=True)

        frame.after(1500, frame.pack_forget)

        return frame
    

class botao_indentificador(ctk.CTkFrame):
    def __init__(self,frame, op, qtd_confirm, status, total, fines, on_click=None):
        super().__init__(frame, fg_color=self.get_cor(status), height=40, width=800)

        self.pack_propagate(False)


        self.botao = ctk.CTkButton(
            self, 
            text=f"   OP: {op}   ",
            fg_color="transparent",
            text_color=cor.DHL_COLORS["text_dark"],
            font=("Arial", 20, "bold"),
            command=lambda: on_click(op) if on_click else None

        )
        self.botao.pack(side="left", anchor="n", fill="both", expand=True)

        #destaca a existencia de fines
        if fines == 1:
            self.label_fines = ctk.CTkLabel(
                self, 
                height=40,
                text="F",
                font=("Arial", 20, "bold"),

            )
            self.label_fines.pack(side="left", padx=40)
        else:
            self.label_fines = ctk.CTkLabel(
                self, 
                height=40,
                text=" ",
                font=("Arial", 20, "bold"),

            )
            self.label_fines.pack(side="left", padx=40)




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
        self.label_status.pack(side="right", padx=20)

    def get_cor(self, status):
        
        if status == "pendente":
            return cor.DHL_COLORS["warning"]
        elif status == "concluido":
            return cor.DHL_COLORS["success"]
        elif status == "cancelado":
            return cor.DHL_COLORS["danger"]




        


    