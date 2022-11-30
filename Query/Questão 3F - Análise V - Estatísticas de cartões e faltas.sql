-- =====================================================================================
-- QUESTÃO 3F - Análise V - Estatística de cartões e faltas
-- =====================================================================================

-- São 3 scripts pra gerar as 3 saídas desta query
-- O que muda é apenas o ORDER BY no final (qty_fouls, qty_carts, percent)
-- Mas eu repliquei as queries para facilitar a execução 

-- -------------------------------------------------
-- 1/3 - Times com maior número de faltas
-- ------------------------------------------------- 
WITH tb_team_fouls AS (
	-- Dados de falta
	SELECT team_api_id
		  ,COUNT(*)		AS qty_fouls
		FROM Match_Fouls
	GROUP BY team_api_id
  ), 
    -- Dados de cartão
	tb_team_cards AS (
	SELECT team_api_id
		  ,COUNT(*)		AS qty_cards
		FROM Match_Cards
	GROUP BY team_api_id
  )
SELECT t.team_long_name   							   AS team
	,tf.qty_fouls
	,tc.qty_cards
	,ROUND(CAST(tc.qty_cards AS REAL)/tf.qty_fouls, 4) AS percent
FROM Team				t
LEFT JOIN tb_team_fouls		tf ON tf.team_api_id = t.team_api_id
LEFT JOIN tb_team_cards		tc ON tc.team_api_id = t.team_api_id	
WHERE qty_fouls > 0	
ORDER BY qty_fouls DESC LIMIT 5 ;
  
  
-- -------------------------------------------------
-- 2/3 - Times com maior número de cartões
-- ------------------------------------------------- 
WITH tb_team_fouls AS (
	-- Dados de falta
	SELECT team_api_id
		  ,COUNT(*)		AS qty_fouls
		FROM Match_Fouls
	GROUP BY team_api_id
  ), 
    -- Dados de cartão
	tb_team_cards AS (
	SELECT team_api_id
		  ,COUNT(*)		AS qty_cards
		FROM Match_Cards
	GROUP BY team_api_id
  )	
SELECT t.team_long_name   							   AS team
	,tf.qty_fouls
	,tc.qty_cards
	,ROUND(CAST(tc.qty_cards AS REAL)/tf.qty_fouls, 4) AS percent
FROM Team				t
LEFT JOIN tb_team_fouls		tf ON tf.team_api_id = t.team_api_id
LEFT JOIN tb_team_cards		tc ON tc.team_api_id = t.team_api_id	
WHERE qty_fouls > 0	
ORDER BY qty_cards DESC LIMIT 5;


-- -------------------------------------------------
-- 3/3 - Times com maior número de cartões recebidos por falta (percent)
-- ------------------------------------------------- 
WITH tb_team_fouls AS (
	-- Dados de falta
	SELECT team_api_id
		  ,COUNT(*)		AS qty_fouls
		FROM Match_Fouls
	GROUP BY team_api_id
  ), 
    -- Dados de cartão
	tb_team_cards AS (
	SELECT team_api_id
		  ,COUNT(*)		AS qty_cards
		FROM Match_Cards
	GROUP BY team_api_id
  )	
SELECT t.team_long_name   							   AS team
	,tf.qty_fouls
	,tc.qty_cards
	,ROUND(CAST(tc.qty_cards AS REAL)/tf.qty_fouls, 4) AS percent
FROM Team				t
LEFT JOIN tb_team_fouls		tf ON tf.team_api_id = t.team_api_id
LEFT JOIN tb_team_cards		tc ON tc.team_api_id = t.team_api_id	
WHERE qty_fouls > 0	
 AND percent < 1   -- Ignorei uma possível sujeira: times que possuem mais cartoes do que faltas
ORDER BY percent DESC LIMIT 5 ;
	
