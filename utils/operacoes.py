from pathlib import Path
import sys
import os 
import tabula
import tabula.io
import pandas as pd
import re

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import config

def achar_arquivo(op):
    misturas_normais_dir = Path(config.APP_PDF).resolve() / "Misturas"

    if not misturas_normais_dir.exists():
        print(f"Pasta não encontrada: {misturas_normais_dir}")
        return "N/A"
    
    padrao = re.compile(r"(\d{7})\.pdf$")

    for nome_arquivo in os.listdir(misturas_normais_dir):
        match = padrao.search(nome_arquivo)
        if match and match.group(1) == op:
            return nome_arquivo
    return "N/A"

def extrair_dados(arquivo):
    caminho = str(Path(config.APP_PDF) / "Misturas" / arquivo)

    # Extrai todas as tabelas do PDF
    tabelas = tabula.io.read_pdf(
        caminho,
        pages="all",
        multiple_tables=True,
        lattice=True,
        guess=False
    )

    # Lista para armazenar DataFrames válidos
    tabelas_com_material = []

    for tabela in tabelas:
        if tabela is not None and "Material" in tabela.columns:
            tabela = tabela.dropna(how="all")  # remove linhas totalmente vazias
            tabelas_com_material.append(tabela)

    if not tabelas_com_material:
        print("Nenhuma tabela com coluna 'Material' encontrada.")
        return pd.DataFrame()

    # Concatena todas as tabelas válidas em um único DataFrame
    df_materiais = pd.concat(tabelas_com_material, ignore_index=True)
    return df_materiais




#Obtem MIsturas normais
def misturas_normais(arquivo):
    df = extrair_dados(arquivo)
    df = df['Material'].dropna().astype(str)
    padrao = re.compile(r"^1.*[a-zA-Z]$")

    materiais_mistura = []

    for cod in df:
        if padrao.match(cod):
            materiais_mistura.append(cod)
            
        else:
            return materiais_mistura
            

        

# Chamada