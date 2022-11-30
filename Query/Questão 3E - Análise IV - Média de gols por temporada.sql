-- =====================================================================================
-- QUESTÃO 3b - Análise IV - Média de gols por temporada por país
-- =====================================================================================

WITH Tb_Season_Data AS (
	SELECT    m.season
			 ,c.name										 	AS country
	         ,ROUND(AVG(m.home_team_goal+m.away_team_goal),2)   AS avg_goals_per_match_home
         FROM Match         m
		 JOIN League        l     ON l.id = m.league_id
		 JOIN Country       c     ON c.id = l.country_id			 
	GROUP BY m.season
		    ,c.name
	ORDER BY m.season
	        ,avg_goals_per_match_home DESC
 )
	SELECT season
	      ,ranking
		  ,country
		  ,avg_goals_per_match_home
		FROM (
				SELECT  season
					   ,ROW_NUMBER() OVER(PARTITION BY season
										  ORDER BY avg_goals_per_match_home DESC, country) AS ranking
					   ,country
					   ,avg_goals_per_match_home		   
					FROM Tb_Season_Data
			  )
	WHERE ranking <=3;
		
	
	