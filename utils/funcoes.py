import datetime
import customtkinter as ctk

def atualizar_relogio(app,relogio):
        agora = datetime.datetime.now().strftime("%H:%M:%S")
        relogio.configure(text=agora)
        app.after(1000, atualizar_relogio)


def focar_campo(app, campo, event=None):
        campo.focus()
        app.after(100, campo.focus)
