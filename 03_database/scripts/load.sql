--RELATORIO_CADOP------------
COPY relatorio_cadop
FROM '/home/brisa/IdeaProjects/IntuitiveCareTest1/03_database/data/Relatorio_cadop.csv'
DELIMITER ';'
ENCODING 'UTF8'
CSV header;

--DEMONSTRACOES_CONTABEIS----------
COPY demonstracoes_contabeis
FROM '/home/brisa/IdeaProjects/IntuitiveCareTest1/03_database/data/1T2023.csv'
DELIMITER ';'
ENCODING 'UTF8'
CSV HEADER;

COPY demonstracoes_contabeis
FROM '/home/brisa/IdeaProjects/IntuitiveCareTest1/03_database/data/2T2023.csv'
DELIMITER ';'
ENCODING 'UTF8'
CSV HEADER;

COPY demonstracoes_contabeis
FROM '/home/brisa/IdeaProjects/IntuitiveCareTest1/03_database/data/3T2023.csv'
DELIMITER ';'
ENCODING 'UTF8'
CSV HEADER;

COPY demonstracoes_contabeis
FROM '/home/brisa/IdeaProjects/IntuitiveCareTest1/03_database/data/4T2023.csv'
DELIMITER ';'
ENCODING 'UTF8'
CSV HEADER;

COPY demonstracoes_contabeis
FROM '/home/brisa/IdeaProjects/IntuitiveCareTest1/03_database/data/1T2024.csv'
DELIMITER ';'
ENCODING 'UTF8'
CSV HEADER;

COPY demonstracoes_contabeis
FROM '/home/brisa/IdeaProjects/IntuitiveCareTest1/03_database/data/2T2024.csv'
DELIMITER ';'
ENCODING 'UTF8'
CSV HEADER;

COPY demonstracoes_contabeis
FROM '/home/brisa/IdeaProjects/IntuitiveCareTest1/03_database/data/3T2024.csv'
DELIMITER ';'
ENCODING 'UTF8'
CSV HEADER;

COPY demonstracoes_contabeis
FROM '/home/brisa/IdeaProjects/IntuitiveCareTest1/03_database/data/4T2024.csv'
DELIMITER ';'
ENCODING 'UTF8'
CSV HEADER;