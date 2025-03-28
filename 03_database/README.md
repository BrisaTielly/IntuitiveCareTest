# Importando Dados para o PostgreSQL no Docker

Este guia ensina como configurar um banco de dados PostgreSQL em um contêiner Docker e carregar automaticamente os arquivos CSV para as tabelas `demonstracoes_contabeis` e `relatorio_cadop`.

---

## **1. Inicializando o Banco de Dados**
Para iniciar o PostgreSQL no Docker, execute:
```bash
docker-compose up -d
```
Isso criará e iniciará o contêiner `intuitive_care_postgres.`.

---

## **3. Criando as Tabelas**
Conecte-se ao PostgreSQL e crie as tabelas necessárias:
```bash
docker exec -it intuitive_care_postgres psql -U admin -d intuitive_care
```
No terminal do PostgreSQL, execute:
```sql
O Script presente em 03_database/scripts/create_tables.sql
```

---

## **4. Carregando os Dados**
Para importar os arquivos CSV automaticamente, vá até cd 03_database e execute:
```bash
for file in ./data/*.csv; do
    if [[ $(basename "$file") == "Relatorio_cadop.csv" ]]; then
        docker exec -i intuitive_care_postgres psql -U admin -d intuitive_care -c "\copy relatorio_cadop FROM '/data/$(basename "$file")' DELIMITER ';' CSV HEADER ENCODING 'UTF8';"
    else
        docker exec -i intuitive_care_postgres psql -U admin -d intuitive_care -c "\copy demonstracoes_contabeis FROM '/data/$(basename "$file")' DELIMITER ';' CSV HEADER ENCODING 'UTF8';"
    fi
done
```

Este comando percorre todos os arquivos CSV dentro do diretório montado no contêiner (`/data`):
- Se o arquivo for `Relatorio_cadop.csv`, ele é carregado na tabela `relatorio_cadop`.
- Caso contrário, ele é carregado na tabela `demonstracoes_contabeis`.

---
