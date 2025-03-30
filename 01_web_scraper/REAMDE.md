# 01 Web Scraping

## Descrição
Este projeto realiza Web Scraping para baixar e compactar arquivos PDF da página da Agência Nacional de Saúde Suplementar (ANS). O objetivo é acessar o site oficial da ANS, identificar os anexos I e II disponíveis para download e armazená-los em um arquivo ZIP.

## Tecnologias Utilizadas
- Python 3
- Requests
- BeautifulSoup (bs4)
- ZipFile (módulo padrão do Python)

## Como Executar
No diretório do projeto: 
```bash
cd 01_web_scraper
```

### 1. Instalação de Dependências
Antes de executar o script, instale as bibliotecas necessárias utilizando o arquivo `requirements.txt`:
```bash
pip install -r requirements.txt
```
Ou instale manualmente:
```bash
pip install requests beautifulsoup4
```

### 2. Execução do Script
Basta rodar o script `scraper.py` para baixar e compactar os PDFs:
```bash
python scraper.py
```
Os arquivos serão armazenados no diretório `anexos/` e compactados no arquivo `anexos.zip`.

## Estrutura do Projeto
```
web_scraping/
│── scraper.py  # Script principal com documentação inline
│── requirements.txt  # Dependências do projeto
│── anexos/  # Diretório onde os PDFs serão armazenados e compactados
```

---


