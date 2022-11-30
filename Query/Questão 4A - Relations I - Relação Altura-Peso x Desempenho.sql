-- =====================================================================================
-- QUESTÃO 4 - Relations I - Ranking de desempenho por faixa de Altura e Peso
-- Os 6 melhores dentre cada uma das três faixas
-- =====================================================================================

-- DROP TABLE Relations;

-- Cria tabela, utilizando overall_rating do attributos mais recentes de cada jogador
-- Separando os jogadores em 3 faixas peso e 3 faixas altura
CREATE TABLE Relations AS 
	WITH Player_Data AS (
		SELECT p.player_api_id
			 , p.player_name
			 , CASE 
					WHEN p.height > 155 AND p.height < 170.99 THEN '155-170'
					WHEN p.height > 171 AND p.height < 185.99 THEN '171-185'
					WHEN p.height > 185 AND p.height < 210.99 THEN '185-210'
			   END				AS range_height_name
			 , CASE 
					WHEN p.weight > 100 AND p.weight < 150.99 THEN '100-150'
					WHEN p.weight > 151 AND p.weight < 200.99 THEN '151-200'
					WHEN p.weight > 200 AND p.weight < 250.99 THEN '200-250'
			   END				AS range_weight_name			 		 
			 , pam.overall_rating
		FROM Player                        p
		JOIN Player_Attributes_Modified    pam ON pam.player_api_id = p.player_api_id
											  AND pam.date = (SELECT MAX(date)
																FROM Player_Attributes_Modified pam2
															   WHERE pam2.player_api_id = pam.player_api_id
															  )

																																  
		ORDER BY p.player_api_id
	)

	-- Ranking por Altura
	SELECT 'Altura' 		 	AS analysis_name
		  ,range_height_name 	AS range
		  ,ranking
		  ,player_name
		  ,overall_rating			  
		FROM  (
				--Ordena para gerar o ranking
				SELECT  range_height_name 
					   ,ROW_NUMBER() OVER (PARTITION BY range_height_name 
											ORDER BY overall_rating DESC, player_name) AS ranking
					   ,player_name
					   ,overall_rating						   
					FROM Player_Data
			   )
	WHERE ranking <= 6
	UNION
	-- Ranking por Peso
	SELECT 'Peso' 		 		AS analysis_name
		  ,range_weight_name 	AS range
		  ,ranking
		  ,player_name
		  ,overall_rating			  
		FROM  ( --Ordena para gerar o ranking
				SELECT  range_weight_name 
					   ,ROW_NUMBER() OVER (PARTITION BY range_weight_name 
											ORDER BY overall_rating DESC, player_name) AS ranking
					   ,player_name
					   ,overall_rating						   
					FROM Player_Data
			   )
	WHERE ranking <= 6		
	;

-- -----------------------------------------------------------------------

	-- ------------------------------
	-- Select na tabela final - Altura
	-- ------------------------------
	SELECT * FROM Relations 
		WHERE analysis_name = 'Altura';

	-- ------------------------------
	-- Select na tabela final - Peso
	-- ------------------------------
	SELECT * FROM Relations 
		WHERE analysis_name = 'Peso';