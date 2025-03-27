import os
import zipfile
import pandas as pd
import pdfplumber

# Lê o PDF e extrai tabelas e converte para DataFrame
def extract_pdf_data(pdf_path):
    print("Iniciando extração de dados do PDF...")
    with pdfplumber.open(pdf_path) as pdf:
        tables = []
        for page in pdf.pages[2:]:
            table = page.extract_table()
            if table and len(table) > 1:
                df = pd.DataFrame(table[1:], columns=table[0])
                tables.append(df)

        return pd.concat(tables, ignore_index=True) if tables else pd.DataFrame()
