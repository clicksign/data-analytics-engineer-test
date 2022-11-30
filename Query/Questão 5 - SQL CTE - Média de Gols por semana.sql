-- =====================================================================================
-- Questão 5 - SQL CTE
-- Média de gols por semana (time mandante e visitante) - Histórico completo
-- =====================================================================================

WITH tb_average AS (
-- Agrupa a média de gols por semana com a função JULIANDAY para saber quando a semana termina (domingo)
-- Ex. os gols de 27/04/2016 (segunda-feira) a 03/05/2016 (domingo), serão agrupados em 03/05/2016
-- Ordena as semanas através do nRow para que se possa calcular o crescimento da semana atual com base na linha anterior nRow-1
	SELECT  
             ROW_NUMBER() OVER(ORDER BY 1) 				AS nRow
			,STRFTIME('%Y', 
					  JULIANDAY(m.date, 'weekday 0'))	AS year 			
			,STRFTIME('%m', 
					  JULIANDAY(m.date, 'weekday 0'))	AS month 			
			,STRFTIME('%Y-%m-%d', 
					  JULIANDAY(m.date, 'weekday 0'))	AS end_of_week    
		   ,ROUND(AVG(home_team_goal),2)      			AS avg_goals_per_match_home
		   ,ROUND(AVG(away_team_goal),2)    			AS avg_goals_per_match_away		   
		 FROM Match         m 
     GROUP BY year
			, month
			, end_of_week       
	ORDER BY year DESC
		   , month DESC 
		   , end_of_week DESC	
					)

-- Exibe a média de gols do mandante e visitante, calculando o crescimento(%), comparando com a média da semana anterior (nRow-1)
-- tbCur: dados da semana atual
-- tbPrev: dados da semana anterior
SELECT tbCur.year
	  ,tbCur.month
      ,tbCur.end_of_week 
      ,tbCur.avg_goals_per_match_home
      ,COALESCE(ROUND((tbCur.avg_goals_per_match_home - tbprev.avg_goals_per_match_home) 
                       /tbprev.avg_goals_per_match_home 
					  ,4),0)									AS 'home_avg_growth %'
      ,tbCur.avg_goals_per_match_away           
      ,COALESCE(ROUND( (tbCur.avg_goals_per_match_away - tbprev.avg_goals_per_match_away) 
                        /tbprev.avg_goals_per_match_away
					  ,4),0)        							AS 'away_avg_growth %'
      FROM tb_average tbCur
 LEFT JOIN tb_average tbprev ON tbprev.nRow = tbCur.nRow-1 ;

