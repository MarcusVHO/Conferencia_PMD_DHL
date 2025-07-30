#Responsavel trabalhar arquivos de pdf 
#Criador: Marcus Vinicius Hilário de Oliveira
#Data: 26/07/2025

#------------------ inportações Externas --------------------
import pdfplumber
import pandas as pd
import re
import os
from tkinter import filedialog
#------------------ inportações Externas --------------------


#------------------ inportações internas --------------------
import model.pmd.inserir_mistura_model as model
from view.components.widgets_reutilizaveis import botao_indentificador
#------------------ inportações internas --------------------


def selecionar_arquivo_misturas_normais( event=None):
    arquivo = filedialog.askopenfilenames(
        title="Selecionar Arquivos Misturas",
        filetypes=(("Arquivos PDFs", "*.pdf"), ("Arquivos PDFs", "*.pdf"))
    )

    

    padrao = re.compile(r"^1.*[a-zA-Z]$")
    coluna_material = "Material"

    if arquivo:
        for arquivo in arquivo:

            #obtem nome do arquivo somente 
            nome_do_arquivo = os.path.basename(arquivo)
            print("Arquivos Selecionados: ", nome_do_arquivo)   

            #padrao para obter numero de op
            match = re.search(r"\d{7,}", nome_do_arquivo)
            
            #obtem apenas opercao
            if match:
                op = match.group()
                print("OP: ", op )
            

            dataframes = [] #reinicia o dataframe para cada aruqivo

            with pdfplumber.open(arquivo) as pdf:
                for i, page in enumerate(pdf.pages):
                    tables = page.extract_tables()
                    for table in tables:
                        if table:
                            header = table[0]
                            if any("Material" in str(col) for col in header):
                                df = pd.DataFrame(table[1:], columns=header)
                                dataframes.append(df)

            if dataframes:
                df_geral = pd.concat(dataframes, ignore_index=True)

                if coluna_material in df_geral.columns:
                    materiais = df_geral[coluna_material].dropna().astype(str)

                    # Encontrar índice de quebra
                    indice_quebra = None
                    for i, material in enumerate(materiais):
                        if not padrao.match(material):
                            indice_quebra = i
                            break

                    # Misturas e Fines separadas
                    misturas = [cod for cod in materiais[:indice_quebra] if padrao.match(cod)]
                    fines = []
                    if indice_quebra is not None:
                        fines = [cod for cod in materiais[indice_quebra+1:] if padrao.match(cod)]

 
                    #printa as misturas 
                    print(f"Misturas: {misturas}")

                    #print da quantidade de intens na mistura
                    total_mist = len(misturas)
                    print("Total de intens na mistura: ", total_mist)

                    #oobtem total de intens fines
                    total_fines = len(fines)
                    print("Total de intens fines: ", total_fines)

                    #inseri todos os dados no banco de dados
                    model.inserir_mistura_normal(op, misturas, total_mist, fines, total_fines)


                else:
                    print(f"Arquivo {arquivo} não contém coluna '{coluna_material}'")
            else:
                print(f"Nenhuma tabela compatível no arquivo {arquivo}")

   
   #obtem lista com misturas normais
def mostrar_misturas_normais(frame, event=None):
    misturas_normais_pendentes = model.listar_misturas_normais_pendentes()

    for mistura in misturas_normais_pendentes:
        #verifica se op tem fines 
        existe_fines = model.verificar_existencia_fines(mistura[0])
        print(existe_fines)

        #cria botoes indentificadores
        botao = botao_indentificador(frame, mistura[0], mistura[1], mistura[2], mistura[3], existe_fines)
        botao.pack(pady=5)

    print(misturas_normais_pendentes)



#inseri sts 
def selecionar_arquivo_sts():
    arquivo = filedialog.askopenfilenames(
    title="Selecionar Arquivos Misturas",
    filetypes=(("Arquivos PDFs", "*.pdf"), ("Arquivos PDFs", "*.pdf"))
    )



    padrao = re.compile(r"^1.*[a-zA-Z]$")
    colunas_interessaveis = ["Material", " Quantity"]

    if arquivo:
        for arquivo in arquivo:

            #obtem nome do arquivo somente 
            nome_do_arquivo = os.path.basename(arquivo)
            print("Arquivos Selecionados: ", nome_do_arquivo)   

            #padrao para obter numero de op
            match = re.search(r"\d{7,}", nome_do_arquivo)
            
            #obtem apenas opercao
            if match:
                op = match.group()
                print("OP: ", op )
            

            dataframes = [] #reinicia o dataframe para cada aruqivo

            with pdfplumber.open(arquivo) as pdf:
                for i, page in enumerate(pdf.pages):
                    tables = page.extract_tables()
                    for table in tables:
                        if table:
                            header = table[0]
                            if any("Material" in str(col) for col in header):
                                df = pd.DataFrame(table[1:], columns=header)
                                dataframes.append(df)


                    
            colunas_interessaveis = ["Material", "Quantity"]

            # Lista para armazenar os dados extraídos
            materiais = []
            quantidades = []

            for df in dataframes:
                # Normaliza o nome das colunas para evitar problemas com espaços
                df.columns = [col.strip() for col in df.columns]
                
                if all(col in df.columns for col in colunas_interessaveis):
                    mat_col = df["Material"].astype(str).dropna()
                    qty_col = df["Quantity"].astype(str).dropna()
                    
                    for m, q in zip(mat_col, qty_col):
                        # Filtra materiais que começam com 1 e terminam com letra
                        if re.match(r"^1.*[a-zA-Z]$", m):
                            materiais.append(m)
                            quantidades.append(q)

            print(materiais, quantidades)

            lista_de_materiais = []

            #expand lista de acordo com quantidade de caixas
            for material, quantidade in zip(materiais, quantidades):

                quantidade = float(quantidade.replace("KG", "".replace(",", ".")))
                peso_caixa = model.obter_peso_caixa(material)
                peso_caixa = float(peso_caixa)


                quntidade_caixas = quantidade/peso_caixa

                lista_de_materiais.extend([material] * int(round(quntidade_caixas)))

            print(lista_de_materiais)


            #obtem total de sts
            total_sts = len(lista_de_materiais)


            #realiza insercoes no banco
            model.inserir_sts(op, lista_de_materiais, total_sts)





   #obtem lista com sts 
def mostrar_sts(frame, event=None):
    sts_pendentes = model.listar_sts_pendentes()

    for sts in sts_pendentes:
        
        #verifica se op tem fines 
        existe_fines = model.verificar_existencia_fines(sts[0])
        print(existe_fines)

        #cria botoes indentificadores
        botao = botao_indentificador(frame, sts[0], sts[1], sts[2], sts[3], 0)
        botao.pack(pady=5)

    print(sts_pendentes)