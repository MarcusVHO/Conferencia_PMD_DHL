#Respnsavel por realizar as funcoes da tela de login
#Criador: Marcus Vinicius Hilário de Oliveira
#Data: 25/07/2025

#------------------ inportações --------------------
import customtkinter as ctk
import config.settings as st
import config.colors as cor
import model.login_model as model
#------------------ inportações --------------------

#------------------ Funcoes -----------------------

#respnsavel por validar login do usuario
def validar_login(username, senha, event=None):
    lista_usuarios = model.buscar_usuarios()
    
    for usuario in lista_usuarios:
        if usuario["idusuario"] == username and usuario["senha"] == senha:
            #remove senha antes de retornar
            usuario.pop("senha")
            st.USUARIO_LOGADO = usuario

            return True, usuario["nomeusuario"]

    return False, "Usuario ou senha invalidos"

    