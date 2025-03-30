# 02 Transformação de Dados

Este diretório contém o código para o teste técnico, que realiza a extração de dados de um PDF, limpa esses dados, salva em formato CSV e compacta o arquivo em um arquivo ZIP. O PDF utilizado para a extração é o Anexo I do teste 1.


## Requisitos

Para rodar este projeto, você precisa ter as seguintes bibliotecas instaladas:

- `pandas`
- `pdfplumber`

Você pode instalar as dependências necessárias utilizando o comando no diretório do projeto:

```bash
pip install -r requirements.txt
```

## Estrutura do Projeto

A estrutura do projeto é a seguinte:

```
/project-directory
│
├── Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf  # PDF de entrada
├── transform_data.py  # Código python para a transformação de dados
├── Teste_brisa.csv  # Arquivo CSV gerado após a extração e limpeza dos dados
├── Teste_brisa.zip  # Arquivo ZIP contendo o CSV
└── requirements.txt  # Arquivo de dependências
```

## Como Executar

1. Execute o código Python com o seguinte comando no diretório de 02_data_transform:

```bash
python scraper.py
```

3. O código irá gerar o arquivo CSV `Teste_brisa.csv` e o arquivo ZIP `Teste_brisa.zip` na mesma pasta.

## Conclusão

Este teste foi realizado para demonstrar habilidades em processamento de dados, extração de informações de PDFs, manipulação de dados com `pandas` e compactação de arquivos.

