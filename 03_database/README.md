# 03 database

Este diretório contém scripts SQL e arquivos CSV para configurar e carregar dados em um banco de dados PostgreSQL, com o objetivo de realizar a análise de despesas de operadoras de plano de saúde.

## Estrutura do Projeto

- **data/**: Contém os arquivos CSV necessários para o carregamento dos dados no banco de dados.
- **scripts/**: Contém os scripts SQL para criar as tabelas no banco de dados e carregar os dados dos arquivos CSV.
- **docker-compose.yml**: Arquivo Docker Compose para criar e rodar o PostgreSQL em um contêiner Docker caso você queira.

---

## Como Usar

### 1. Iniciar o Banco de Dados

Se você deseja testar o banco de dados no Docker, execute o seguinte comando no diretório desse projeto (03_database) do para iniciar o contêiner PostgreSQL:

```bash
docker-compose up -d
```

Isso criará e iniciará o contêiner `intuitive_care_postgres`.

### 2. Criar as Tabelas no Banco de Dados

Conecte-se ao contêiner PostgreSQL:

```bash
docker exec -it intuitive_care_postgres psql -U admin -d intuitive_care
```

No terminal do PostgreSQL, execute o script para criar as tabelas:

```sql
\i /scripts/create_tables.sql
```

Isso criará as tabelas necessárias para armazenar os dados dos arquivos CSV.

### 3. Carregar os Dados

Para carregar os dados dos arquivos CSV no banco de dados, execute o seguinte comando:

```bash
for file in ./data/*.csv; do
    if [[ $(basename "$file") == "Relatorio_cadop.csv" ]]; then
        docker exec -i intuitive_care_postgres psql -U admin -d intuitive_care -c "\copy relatorio_cadop FROM '/data/$(basename "$file")' DELIMITER ';' CSV HEADER ENCODING 'UTF8';"
    else
        docker exec -i intuitive_care_postgres psql -U admin -d intuitive_care -c "\copy demonstracoes_contabeis FROM '/data/$(basename "$file")' DELIMITER ';' CSV HEADER ENCODING 'UTF8';"
    fi
done
```

Esse comando percorre todos os arquivos CSV dentro da pasta `data/` e importa os dados nas tabelas correspondentes.

---


## Conclusão

Esse repositório fornece todas as etapas necessárias para configurar um banco de dados PostgreSQL e realizar análises sobre as despesas das operadoras de planos de saúde, utilizando dados extraídos de arquivos CSV da ANS.

---

## Arquivos

- **scripts/create_tables.sql**: Cria as tabelas no banco de dados.
- **scripts/load.sql**: Carrega os dados dos arquivos CSV para as tabelas no banco de dados.
- **scripts/analytics_querys.sql**: Contém as consultas analíticas para as maiores despesas.
- **docker-compose.yml**: Arquivo para iniciar o banco de dados PostgreSQL em um contêiner Docker.
- **data/**: Pasta contendo os arquivos CSV com os dados necessários.

```

Esse README contém uma explicação clara e objetiva sobre como preparar e utilizar o repositório. Deixei as instruções simples e diretas, já que o foco é mostrar como usar o projeto. Se precisar de mais detalhes ou ajustes, só avisar!