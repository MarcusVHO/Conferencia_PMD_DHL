from pathlib import Path
import sys
import os 
import pandas as pd
import re
import pdfplumber
import customtkinter as ctk
import winsound

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import config
import utils.funcoes as func

def achar_arquivo(op, pasta):
    if pasta == "misturas":
        misturas_normais_dir = Path(config.APP_PDF).resolve() / "Misturas"
    elif pasta == "sts":
        misturas_normais_dir = Path(config.APP_PDF).resolve() / "STS"

    if not misturas_normais_dir.exists():
        print(f"Pasta não encontrada: {misturas_normais_dir}")
        return "N/A"
    
    padrao = re.compile(r"(\d{7})\.pdf$")

    for nome_arquivo in os.listdir(misturas_normais_dir):
        match = padrao.search(nome_arquivo)
        if match and match.group(1) == op:
            return nome_arquivo
    return "N/A"

def extrair_dados(arquivo, pasta):
    
    if pasta == "misturas":
        caminho = config.APP_PDF / "Misturas" / arquivo
    elif pasta == "sts":
        caminho = config.APP_PDF / "STS" / arquivo

    dataframes = []
    if not Path(caminho).exists():
        print(f"Arquivo não encontrado: {arquivo}")
        return pd.DataFrame()
    with pdfplumber.open(caminho) as pdf:
        for i, page in enumerate(pdf.pages):
            tables = page.extract_tables()
            for table in tables:
                if table:
                    header = table[0]
                    if any("Material" in str(col) for col in header):
                        df = pd.DataFrame(table[1:], columns=header)
                        dataframes.append(df)
    if dataframes:
        df_geral=pd.concat(dataframes, ignore_index=True)
    
    else:
        df_geral=pd.DataFrame()

    return df_geral


#Obtem MIsturas normais
def misturas_normais(arquivo):
    df = extrair_dados(arquivo, "misturas")
    df = df['Material'].dropna().astype(str)
    padrao = re.compile(r"^1.*[a-zA-Z]$")

    materiais_mistura = []

    for cod in df:
        if padrao.match(cod):
            materiais_mistura.append(cod)
            
        else:
            return materiais_mistura
            

#Obtem Fines das misturas
def obter_fines(arquivo):
    df = extrair_dados(arquivo, "misturas")
    df = pd.DataFrame(df)

    coluna_material = "Material"
    padrao = re.compile(r"^1.*[a-zA-Z]$")

    materiais_fines = []

    indice_quebra = None

    for i, material in enumerate(df[coluna_material]):
        if not padrao.match(str(material)):
            indice_quebra = i
            break
    materiais_fines = df.iloc[indice_quebra +1:][coluna_material]
    df_resultado = materiais_fines[materiais_fines.astype(str).str.match(padrao)]
    df_resultado = df_resultado.reset_index(drop=True)
    return df_resultado
        

#def obter sts
def obter_sts(arquivo):
    #extrai dataframe do arquivo
    df = extrair_dados(arquivo, "sts")
    
    #descarta informações desnecessarias
    colunas_necessarias = ['Material', 'Quantity']
    df = df[colunas_necessarias]
    df = df.dropna()
    
    #filtra materiais 
    padrao = re.compile(r"^1.*[a-zA-Z]$")
    df = df[df["Material"].astype(str).str.match(padrao)].reset_index(drop=True)
    df["Quantity"] = df["Quantity"].astype(str).str.replace(r"[^\d.,]", "", regex=True).str.replace(",", ".")
    df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce")
    
    return df

    



if __name__ == "__main__":
    app = ctk.CTk()
    app.geometry(config.APP_SIZE)

    janela = cirar_lista_item("104090x",1600)
    app.mainloop()