-- =====================================================================================
-- QUESTÃO 4 - Relations II - Extra: Relação Idade x Média de desempenho 
-- Jogadores de 18 a 40 anos
-- =====================================================================================
WITH Player_Data AS (
	SELECT player_api_id
		  ,CASE 
				WHEN age >= 18 AND age <= 25 THEN '18-25'
				WHEN age >= 26 AND age <= 30 THEN '26-30'
				WHEN age >= 31 AND age <= 35 THEN '31-35'
				WHEN age >= 36 AND age <= 40 THEN '36-40'
				WHEN age >= 41 AND age <= 45 THEN '41-45'
		   END AS age_range
		  ,AVG(overall_rating) AS overall_rating
		FROM (
				-- Obtem o attributo mais recente de cada jogador
				-- Calcula a idade para facilitar a escrita do CASE ACIMA
				SELECT p.player_api_id
					 , FLOOR( (JULIANDAY( 'now' ) - JULIANDAY(birthday)) /365.25) AS age 
					 , pam.overall_rating
				FROM Player                        p
				JOIN Player_Attributes_Modified    pam ON pam.player_api_id = p.player_api_id
													  AND pam.date = (SELECT MAX(date)
																		FROM Player_Attributes_Modified pam2
																	   WHERE pam2.player_api_id = pam.player_api_id
																		)

																															  
				ORDER BY p.player_api_id
			 )
		WHERE age >18 
		  AND age <=45
        GROUP BY age_range 
)
	-- Resultado: Agrupa por Range e calcula a média de desempenho
	SELECT age_range 				
		  ,ROUND(overall_rating,2) 	AS overall_rating 
		FROM Player_Data
	GROUP BY age_range ;