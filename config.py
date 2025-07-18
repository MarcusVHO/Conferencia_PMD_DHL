from pathlib import Path
import os
import sys


def resource_path(relative_path):
    """Pega o caminho absoluto, considerando o bundle do PyInstaller"""
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


#Configurações Geral do app

APP_TITLE = "Sistema PMD"
APP_SIZE = "1470x730"
APP_THEME = "light"


#Caminhos 
BASE_DIR = Path(__file__).resolve().parent
APP_ICO = resource_path("assets/iconeDHL.ico")
APP_ICO_PNG = resource_path("assets/iconeDHL.png")
APP_PDF = Path(resource_path("PDF"))
APP_FONTE = ("Arial", 20)

#Cores do app
CORES = {
    "primaria": "#FFCC00",      # Amarelo DHL
    "secundaria": "#D40511",    # Vermelho DHL
    "texto": "#000000",         # Preto
    "fundo": "#FFFFFF",         # Branco
    "borda": "#CCCCCC",         # Cinza claro
    "sucesso": "#28a745",       # Verde
    "erro": "#DC3545",          # Vermelho escuro
}