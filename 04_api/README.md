
# 04 API

Este projeto tem como objetivo fornecer uma interface de busca interativa para pesquisar operadoras, usando uma API em FastAPI no backend e um frontend construído com Vue.js. O backend realiza a busca em uma base de dados utilizando texto completo, e o frontend oferece uma interface amigável para os usuários interagirem com a API.

## Tecnologias Utilizadas

- **Frontend**: Vue.js
- **Backend**: FastAPI
- **Banco de Dados**: PostgreSQL
- **Deploy**: AWS S3, AWS RDS, AWS EC2 e CloudFront

## Link para a aplicação completa:

A aplicação completa está [aqui](http://intuitivecarefront.s3-website.us-east-2.amazonaws.com/).

Caso queria rodar a aplicação localmente, as instruções estarão mais abaixo.

## Funcionalidades

### Backend (API)
O backend é responsável por fornecer uma API para buscar operadoras de telefonia com base em um termo de pesquisa. A busca é realizada no banco de dados utilizando uma consulta de texto completo para localizar as operadoras mais relevantes.

### Frontend (Interface Web)
O frontend permite que o usuário insira um termo de busca (nome da operadora) e selecione o número máximo de resultados a serem retornados. Os resultados são exibidos com detalhes adicionais, como CNPJ, modalidade, telefone e endereço da operadora.

## Endpoints da API

### 1. **GET /search**

Este endpoint realiza a busca de operadoras de acordo com o termo fornecido na query `query`.

**Parâmetros**:
- `query`: O termo para busca (obrigatório).
- `maxResults`: O número máximo de resultados a serem retornados. O valor padrão é 10, e o máximo permitido é 50.

**Exemplo de uso**:
```bash
GET /search?query=2b&maxResults=10
```

### Exemplo de resposta:
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

## Como Rodar o Backend Localmente

### Requisitos:
- Python 3.8+
- Banco de Dados PostgreSQL (podendo utilizar o do teste 03)

### Passos para rodar:

1. Clone o repositório:
    ```bash
    git clone <https://github.com/BrisaTielly/IntuitiveCareTest>
    cd <04_api/backend>
    ```

2. Crie e ative um ambiente virtual:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # Linux/Mac
    venv\Scripts\activate     # Windows
    ```

3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

4. Inicie o servidor FastAPI na pasta backend:
    ```bash
    uvicorn main:app --reload
    ```

6. O backend estará disponível em `http://localhost:8000`.

## Como Rodar o Frontend Localmente

### Requisitos:
- Node.js 14+ (inclui o NPM)

### Passos para rodar:

1. Clone o repositório:
    ```bash
    git clone <https://github.com/BrisaTielly/IntuitiveCareTest>
    cd <04_api/frontend>
    ```

2. Instale as dependências:
    ```bash
    npm install
    ```

3. Inicie o servidor de desenvolvimento:
    ```bash
    npm run serve
    ```

4. O frontend estará disponível em `http://localhost:8080`.

## Como Testar com Postman

Você pode importar a coleção do Postman para testar os endpoints da API de forma simples e visual. A coleção está disponível no arquivo `postman_collection.json`.

### Passos:

1. Abra o Postman.
2. Importe a coleção do arquivo `postman_collection.json`.
3. Realize as requisições para testar os endpoints.


