#inportacoes
from pathlib import Path
import os
import sys

#difinicoes de caminho
def diretorio_arquivo_exe():
    if getattr(sys, "frozen", False):
        return Path(sys.executable).resolve().parent
    else:
        return Path(__file__).resolve().parent

def resource_path(relative_path):
    """Pega o caminho absoluto, considerando o bundle do PyInstaller"""
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


#Variaveis do ususario
USUARIO_LOGADO = None

#variaveis gerais do sistema
APP_TITLE = "Sistema de Apoio Operacional"
APP_SIZE = "1470x730"
APP_THEME = "light"

#Caminhos

BASE_DIR = Path(__file__).resolve().parent

APP_ICO = resource_path("assets/iconeDHL.ico")
APP_ICO_PNG = resource_path("assets/iconeDHL.png")
APP_IMG_PESSOA = resource_path("assets/icone_pessoa.png")
APP_IMG_CARRETINHA = resource_path("assets/carretinha.png")
APP_IMG_TRANSPALETE = resource_path("assets/transpalete.png")
APP_IMG_CARRETA = resource_path("assets/carreta.png")
APP_IMG_COLETOR = resource_path("assets/coletor.png")
APP_IMG_CLAMPS = resource_path("assets/clamps.png")
APP_IMG_CAIXA_C48 = resource_path("assets/caixa_c48.png")
APP_IMG_ENGRENAGEM = resource_path("assets/engrenagem.png")
APP_IMG_PRANCHETA = resource_path("assets/prancheta.png")

APP_PDF = diretorio_arquivo_exe() / "PDF"


#Variaveis Genericas
APP_FONTE = ("Arial", 20)