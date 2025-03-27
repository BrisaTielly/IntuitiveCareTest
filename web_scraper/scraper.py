import os
import requests
from bs4 import BeautifulSoup
from zipfile import ZipFile
from urllib.parse import urlparse

# Função para garantir que o diretório de destino exista
def ensure_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

# Função para buscar os links dos anexos I e II
def extract_annex_links(soup, base_url):
    annex_links = []
    for link in soup.find_all("a", href=True):
        text = link.get_text(strip=True).lower()
        href = link["href"]
        if "anexo i" in text or "anexo ii" in text:
            if href.endswith(".pdf"):
                if not href.startswith("http"):
                    href = base_url + href
                annex_links.append(href)
    return annex_links


# Função para baixar os PDFs e compactá-los
def download_and_zip_pdfs(annex_links, zip_path, download_folder):
    ensure_directory(download_folder)  # Cria o diretório para armazenar os PDFs

    with ZipFile(zip_path, "w") as zipf:
        for pdf_url in annex_links:
            file_name = os.path.basename(urlparse(pdf_url).path)
            print(f"Baixando: {file_name}")
            response = requests.get(pdf_url)
            response.raise_for_status()

            # Salva o PDF temporariamente antes de adicionar ao ZIP
            file_path = os.path.join(download_folder, file_name)
            with open(file_path, "wb") as file:
                file.write(response.content)
            
            # Adiciona ao arquivo ZIP
            zipf.write(file_path, file_name)
            os.remove(file_path)  # Remove o PDF temporário após compactar

    print(f"{len(annex_links)} anexos baixados e compactados em '{zip_path}'.")

# Caminho para o diretório 'web_scraper'
base_directory = os.path.dirname(os.path.realpath(__file__))
destination_folder = os.path.join(base_directory, "anexos")
zip_file_path = os.path.join(destination_folder, "anexos.zip")
