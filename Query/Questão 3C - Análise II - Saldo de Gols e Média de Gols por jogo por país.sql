-- =====================================================================================
-- QUESTÃO 3B - Análise II - TOP 3 País com melhor saldo de gols e País com melhor média
-- =====================================================================================
	
	-- -----------------------------------------------------
	-- Top 3 - Países com maior saldo de gols
	-- -----------------------------------------------------
	SELECT  c.name 												   AS country
		   ,SUM(m.home_team_goal + m.away_team_goal)               AS number_of_goals       
		 FROM Match         m
		 JOIN League        l     ON l.id = m.league_id
		 JOIN Country       c     ON c.id = l.country_id
	GROUP BY c.name
	ORDER BY number_of_goals DESC LIMIT 3
	;
	
	-- -----------------------------------------------------
	-- Top 3 - Países com maior média de gols por jogo
	-- -----------------------------------------------------
	SELECT  c.name 												   AS country
		   ,ROUND(AVG(m.home_team_goal + m.away_team_goal),2)      AS avg_goals_per_match	
		   ,SUM(m.home_team_goal + m.away_team_goal)               AS number_of_goals
		   ,COUNT(*)                                               AS number_of_matches       
		 FROM Match         m
		 JOIN League        l     ON l.id = m.league_id
		 JOIN Country       c     ON c.id = l.country_id
	GROUP BY c.name
	ORDER BY avg_goals_per_match DESC  LIMIT 3
	;	
