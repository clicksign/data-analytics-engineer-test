-- =====================================================================================
-- QUESTÃO 3B - Análise II - Time com melhor média de gols: em casa, fora de casa, geral
-- =====================================================================================
	-- -----------------------------------------------------
	-- Time com melhor média de gols EM CASA
	-- -----------------------------------------------------
	SELECT  t.team_long_name 									   AS Team
		   ,SUM(m.home_team_goal)                                  AS number_of_goals_home
		   ,COUNT(*)                                               AS number_of_matches_home       
		   ,ROUND(AVG(m.home_team_goal),2)      AS avg_goals_per_match_home
		 FROM Match         m
		 JOIN League        l     ON l.id = m.league_id
		 JOIN Country       c     ON c.id = l.country_id
                        JOIN Team          t     ON t.team_api_id = m.home_team_api_id         
	GROUP BY t.team_long_name
	ORDER BY avg_goals_per_match_home DESC LIMIT 3 ;	
	
	
	-- -----------------------------------------------------
	-- Time com melhor média de gols como VISITANTE
	-- -----------------------------------------------------
	SELECT  t.team_long_name 									   AS Team
		   ,SUM(m.away_team_goal)                                  AS number_of_goals_away
		   ,COUNT(*)                                               AS number_of_matches_away      
		   ,ROUND(AVG(m.away_team_goal),2)      AS avg_goals_per_match_away
		 FROM Match         m
		 JOIN League        l     ON l.id = m.league_id
		 JOIN Country       c     ON c.id = l.country_id
                        JOIN Team          t     ON t.team_api_id = m.home_team_api_id         
	GROUP BY t.team_long_name
	ORDER BY avg_goals_per_match_away DESC LIMIT 3;		
 	
	
	-- -----------------------------------------------------
	-- Time com melhor média de gols GERAL (EM CASA e como VISITANTE)
	-- -----------------------------------------------------
	WITH tb_team_performance AS (
		SELECT  t.team_long_name 			AS Team
			   ,SUM(m.away_team_goal)       AS number_of_goals_away
			   ,COUNT(*)                    AS number_of_matches_away
			   ,0							AS number_of_goals_home
			   ,0						    AS number_of_matches_home
			 FROM Match         m
			 JOIN League        l     ON l.id = m.league_id
			 JOIN Country       c     ON c.id = l.country_id
		     JOIN Team          t     ON t.team_api_id = m.away_team_api_id         
		GROUP BY t.team_long_name
		UNION
		SELECT  t.team_long_name 					AS Team
			   ,0       							AS number_of_goals_away
			   ,0                   				AS number_of_matches_away	
			   ,SUM(m.home_team_goal)               AS number_of_goals_home
			   ,COUNT(*)                            AS number_of_matches_home       
			 FROM Match         m
			 JOIN League        l     ON l.id = m.league_id
			 JOIN Country       c     ON c.id = l.country_id
			 JOIN Team          t     ON t.team_api_id = m.home_team_api_id         	

		)
	SELECT Team
		  ,SUM(number_of_goals_home + number_of_goals_away)       			AS number_of_goals
		  ,SUM(number_of_matches_home + number_of_matches_away)	  			AS number_of_matches
		  ,ROUND(SUM(number_of_goals_home + number_of_goals_away) /
			     SUM(number_of_matches_home + number_of_matches_away),2)  	AS avg_gols_per_match	  
		FROM tb_team_performance
	 GROUP BY Team
	 ORDER BY avg_gols_per_match DESC LIMIT 3;
	 