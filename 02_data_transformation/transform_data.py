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

# Remove espaços em branco, renomeia colunas e padroniza valores
def clean_dataframe(df):
    if df.empty:
        return df

    print("Iniciando limpeza do DataFrame...")
    df = df.copy()

    for col in df.select_dtypes(include='object'):
        df[col] = df[col].str.strip()

    column_map = {'OD': 'Seguro Odontológico', 'AMB': 'Seguro Ambulatorial'}
    df.rename(columns=column_map, inplace=True)

    return df.replace(column_map)

# Usa codificação utf-8-sig para preservar caracteres especiais
def save_to_csv(df, path):
    if not df.empty:
        print("Salvando dados no CSV...")
        df.to_csv(path, index=False, encoding='utf-8-sig')

# Compacta o arquivo CSV gerado
def create_zip(csv_path, zip_path):
    if os.path.exists(csv_path):
        print("Criando arquivo ZIP...")
        with zipfile.ZipFile(zip_path, 'w') as zipf:
            zipf.write(csv_path, os.path.basename(csv_path))


# Definição de caminhos
pdf_path = 'Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf'
csv_path = 'Teste_brisa.csv'
zip_path = 'Teste_brisa.zip'

# Execução das funções
df = extract_pdf_data(pdf_path)

if not df.empty:
    df = clean_dataframe(df)
    save_to_csv(df, csv_path)
    create_zip(csv_path, zip_path)
    
    print("Processamento concluído.")