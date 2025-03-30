--MAIORES DESPESAS NO ULTIMO TRIMESTRE-----------------------
select
	rc.registro_ans,
    rc.razao_social,
    descricao,
    SUM(
        CAST(REPLACE(REPLACE(dc.vl_saldo_inicial, '.', ''), ',', '.') AS NUMERIC) -
        CAST(REPLACE(REPLACE(dc.vl_saldo_final, '.', ''), ',', '.') AS NUMERIC)
    ) AS despesas
FROM demonstracoes_contabeis dc
INNER JOIN relatorio_cadop rc ON dc.reg_ans = rc.registro_ans
WHERE
    EXTRACT(YEAR FROM dc.data) = 2024
    AND EXTRACT(QUARTER FROM dc.data) = (SELECT MAX(EXTRACT(QUARTER FROM data)) FROM demonstracoes_contabeis WHERE EXTRACT(YEAR FROM data) = 2024)
    AND dc.descricao ILIKE '%EVENTOS%SINISTROS%CONHECIDOS%OU%AVISADOS%'
GROUP BY registro_ans, rc.razao_social, descricao
ORDER BY despesas DESC
LIMIT 10;


--MIORES DESPESAS NO ULTIMO ANO----------------------
SELECT
    rc.registro_ans,
    rc.razao_social,
    descricao,
     SUM(
         CAST(REPLACE(REPLACE(vl_saldo_inicial, '.', ''), ',', '.') AS NUMERIC) -
         CAST(REPLACE(REPLACE(vl_saldo_final, '.', ''), ',', '.') AS NUMERIC)
     ) AS despesas
 FROM demonstracoes_contabeis dc
 INNER JOIN relatorio_cadop rc ON dc.reg_ans = rc.registro_ans
 WHERE EXTRACT(YEAR FROM data) = 2024
 AND descricao ILIKE '%EVENTOS%SINISTROS%CONHECIDOS%OU%AVISADOS%'
 GROUP BY registro_ans, rc.razao_social, descricao
 ORDER BY despesas DESC
 LIMIT 10;
