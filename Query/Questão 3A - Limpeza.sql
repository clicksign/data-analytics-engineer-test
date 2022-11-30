-- =====================================================================================
-- QUESTÃO 3A - Limpeza
-- =====================================================================================

	-- Identifica Paises duplicados pelo ID
	SELECT id, COUNT(*) AS Qty
		FROM Country
	GROUP BY id 
	HAVING COUNT(*)> 1;
	
	-- Apaga países vazios ou com nomes em Portugues, pois já há o equivalente em ingles
	DELETE FROM Country WHERE name = '';
	DELETE FROM Country WHERE Name IN ('Alemanha','Bélgica','França', 'Inglaterra', 'Itália');
	
	-- Apaga as ligas que não possuem Country_ID válido
	DELETE FROM League WHERE Country_Id NOT IN (SELECT id FROM Country);
	
	-- Apaga as partidas que não possuem League_id válido (não há)
	DELETE FROM Match WHERE League_id NOT IN (SELECT id FROM League);
	
	-- Apaga os attributes com JSON inválido
	-- Ex. Há JSON com valores = NaN (attacking_work_rate)
 	DELETE FROM Player_Attributes WHERE JSON_VALID(Player_Attributes) = 0;  -- 3624 de 180354
	DELETE FROM Team_Attributes WHERE JSON_VALID(Team_Attributes) = 0; --971 de 1460
	
	