# Intuitive Care - Teste Técnico

## 📋 Descrição Geral
Este repositório contém a solução completa para o teste técnico na Intuitive Care, abordando um pipeline de dados completo:

* **Web Scraping** para coleta automatizada de dados
* **Transformação de Dados** para extração e limpeza de informações de PDFs
* **Banco de Dados** para armazenar e processar informações estruturadas
* **API Backend** para busca de operadoras de plano de saúde
* **Frontend** para consumir e exibir os dados da API

Cada módulo está em seu próprio diretório com componentes e instruções específicas.

## 🌐 Acesso à Aplicação Online
A aplicação final pode ser acessada diretamente em:  
[**Clique aqui para acessar a aplicação**](http://intuitivecarefront.s3-website.us-east-2.amazonaws.com/)

> **Nota:** Não é necessário executar localmente. Acesse diretamente pelo link acima.

## 📂 Estrutura do Projeto

```
.idea/
01_web_scraper/
    ├── scraper.py              # Script principal para Web Scraping
    ├── requirements.txt        # Dependências do projeto
    ├── anexos/                 # Diretório onde os PDFs serão armazenados e compactados
02_data_transformation/
    ├── transform_data.py       # Código para extração e transformação dos dados
    ├── Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf  # PDF original
    ├── Teste_brisa.csv         # Arquivo CSV gerado
    ├── Teste_brisa.zip         # Arquivo ZIP contendo o CSV
    ├── requirements.txt        # Dependências
03_database/
    ├── scripts/
        ├── create_tables.sql   # Criação de tabelas
        ├── load.sql            # Importação dos dados
        ├── analytics_querys.sql # Consultas analíticas
    ├── docker-compose.yml      # Configuração do PostgreSQL no Docker
    ├── data/                   # Arquivos CSV
04_api/
    ├── backend/                # API FastAPI
    ├── frontend/               # Interface Vue.js
    ├── postman_collection/     # Coleção para testes da API
    ├── readme/                 # Documentação adicional
```

## 🛠️ Tecnologias Utilizadas

### Infraestrutura Cloud
O projeto foi implantado na **AWS** utilizando **EC2, S3, RDS e CloudFront** para garantir escalabilidade, confiabilidade e desempenho.

### Bibliotecas e Frameworks

#### Python
* **`requests`** e **`BeautifulSoup`**: Para Web Scraping eficiente
* **`pdfplumber`**: Para extração precisa de tabelas em PDFs (superior ao `PyPDF2`)
* **`pandas`**: Para manipulação robusta de dados
* **`FastAPI`**: Para desenvolvimento da API, escolhida pela alta performance e suporte a OpenAPI
* **`SQLAlchemy`**: ORM poderoso para manipulação do banco de dados

#### Banco de Dados
* **PostgreSQL**: Banco de dados relacional confiável e escalável
* **Docker**: Para facilitar a execução do banco e garantir reprodutibilidade

#### Frontend
* **Vue.js**: Framework para criar uma interface responsiva e moderna

## 📚 Módulos do Projeto

### 1. Web Scraping
Este módulo acessa o site da Agência Nacional de Saúde Suplementar (ANS), identifica e baixa os anexos I e II em PDF e os compacta.

#### Funcionalidades:
- Acesso automatizado ao site da ANS
- Identificação e download dos PDFs relevantes
- Compactação dos arquivos em um ZIP

### 2. Transformação de Dados
Este módulo extrai, transforma e limpa dados do PDF do Anexo I, gerando um arquivo CSV estruturado.

#### Funcionalidades:
- Extração de tabelas do PDF usando pdfplumber
- Limpeza e transformação dos dados
- Exportação para CSV e compactação

### 3. Banco de Dados
Este módulo configura um banco de dados PostgreSQL e carrega os dados extraídos para análise.

#### Funcionalidades:
- Criação das tabelas necessárias
- Importação dos dados de arquivos CSV
- Consultas analíticas para extrair insights

### 4. API e Frontend
Este módulo fornece uma interface de busca interativa para pesquisar operadoras de planos de saúde.

#### Funcionalidades:
- **Backend**: API FastAPI para busca de operadoras com pesquisa de texto completo
- **Frontend**: Interface Vue.js responsiva e amigável
- **Endpoints**:
  - `GET /search`: Busca operadoras com base em um termo de pesquisa

## 🚀 Instruções de Execução

### 1. Web Scraping
```bash
cd 01_web_scraper
pip install -r requirements.txt
python scraper.py
```

### 2. Transformação de Dados
```bash
cd 02_data_transformation
pip install -r requirements.txt
python transform_data.py
```

### 3. Banco de Dados
```bash
cd 03_database
docker-compose up -d
docker exec -it intuitive_care_postgres psql -U admin -d intuitive_care -c "\i /scripts/create_tables.sql"
docker exec -it intuitive_care_postgres psql -U admin -d intuitive_care -c "\i /scripts/load.sql"
docker exec -it intuitive_care_postgres psql -U admin -d intuitive_care -c "\i /scripts/analytics_querys.sql"
```

### 4. API e Frontend

#### Backend:
```bash
cd 04_api/backend
pip install -r requirements.txt
uvicorn main:app --reload
```
O backend estará disponível em `http://localhost:8000`

#### Frontend:
```bash
cd 04_api/frontend
npm install
npm run serve
```
O frontend estará disponível em `http://localhost:8080`

### 5. Testes com Postman
1. Abra o Postman
2. Importe a coleção do arquivo `04_api/postman_collection/postman_collection.json`
3. Execute as requisições para testar os endpoints

## 📝 Exemplo de Resposta da API

```json
{
  "results": [
    {
      "registro_ans": "421545",
      "cnpj": "22869997000153",
      "razao_social": "2B ODONTOLOGIA OPERADORA DE PLANOS ODONTOLÓGICOS LTDA",
      "nome_fantasia": null,
      "modalidade": "Odontologia de Grupo",
      "logradouro": "RUA CATÃO",
      "numero": "128",
      "complemento": "SALA 126",
      "bairro": "VILA ROMANA",
      "cidade": "São Paulo",
      "uf": "SP",
      "cep": "05049000",
      "ddd": "11",
      "telefone": "34415852",
      "fax": null,
      "endereco_eletronico": "labmarisol@gmail.com",
      "representante": "MARISOL BECHELLI",
      "cargo_representante": "SÓCIO ADMINISTRADORA",
      "regiao_de_comercializacao": "4",
      "data_registro_ans": "2019-06-13"
    }
  ]
}
```

---

© 2025 Teste Técnico - Intuitive Care