from screens.tela_inicial import Tela_Inicial
from screens.menu_conferencia import Menu_Conferencia
from screens.conferencia_misturas import Conferencia_Misturas

tela_inicial = Tela_Inicial()
menu_conferencia = Menu_Conferencia()
conferencia_misturas = Conferencia_Misturas()

tela_inicial.abrir()

# navegador principal
if tela_inicial.opcao == "conferencia":
    menu_conferencia.abrir()
    if menu_conferencia.opcao == "1":
        conferencia_misturas.abrir()