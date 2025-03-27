--RELATORIO_CADOP------------
copy relatorio_cadop
from '/home/brisa/IdeaProjects/IntuitiveCareTest1/03_database/data/Relatorio_cadop.csv'
delimiter ';'
csv header;

--DEMONSTRACOES_CONTABEIS----------
COPY demonstracoes_contabeis
FROM '/home/brisa/IdeaProjects/IntuitiveCareTest1/03_database/data/1T2023.csv'
DELIMITER ';'
ENCODING 'latin1'
CSV HEADER;

COPY demonstracoes_contabeis
FROM '/home/brisa/IdeaProjects/IntuitiveCareTest1/03_database/data/2T2023.csv'
DELIMITER ';'
ENCODING 'latin1'
CSV HEADER;

COPY demonstracoes_contabeis
FROM '/home/brisa/IdeaProjects/IntuitiveCareTest1/03_database/data/3T2023.csv'
DELIMITER ';'
ENCODING 'latin1'
CSV HEADER;

COPY demonstracoes_contabeis
FROM '/home/brisa/IdeaProjects/IntuitiveCareTest1/03_database/data/4T2023.csv'
DELIMITER ';'
ENCODING 'latin1'
CSV HEADER;

COPY demonstracoes_contabeis
FROM '/home/brisa/IdeaProjects/IntuitiveCareTest1/03_database/data/1T2024.csv'
DELIMITER ';'
ENCODING 'latin1'
CSV HEADER;

COPY demonstracoes_contabeis
FROM '/home/brisa/IdeaProjects/IntuitiveCareTest1/03_database/data/2T2024.csv'
DELIMITER ';'
ENCODING 'latin1'
CSV HEADER;

COPY demonstracoes_contabeis
FROM '/home/brisa/IdeaProjects/IntuitiveCareTest1/03_database/data/3T2024.csv'
DELIMITER ';'
ENCODING 'latin1'
CSV HEADER;

COPY demonstracoes_contabeis
FROM '/home/brisa/IdeaProjects/IntuitiveCareTest1/03_database/data/4T2024.csv'
DELIMITER ';'
ENCODING 'latin1'
CSV HEADER;