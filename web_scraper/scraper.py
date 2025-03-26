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
