-- =====================================================================================
-- QUESTÃO 3B - Análise I - Proporção e Comparação: Destro x Canhoto
-- =====================================================================================


WITH Tb_Total AS (
		-- CTE com a quantidade total de jogadores distintos que possuem attributos
        SELECT CAST(COUNT(DISTINCT(player_api_id)) AS FLOAT) AS qtyTotalPlayers
            FROM Player_Attributes_Modified
)
-- Utilizando os atributos mais recents de cada jogador,
-- calcula a média de cada atributo, agrupando por canhotos x destros
-- E calcula a porcentagem de jogadores que jogam com cada pé
SELECT pam.preferred_foot
     , COUNT(DISTINCT(pam.player_api_id))       AS qty_players
     , ROUND(COUNT(DISTINCT(pam.player_api_id))  
			/ tbt.qtyTotalPlayers 	    ,4)     AS percentage
     , ROUND(AVG(pam.finishing)         ,2)     AS finishing
     , ROUND(AVG(pam.free_kick_accuracy),2)     AS free_kick_accuracy
     , ROUND(AVG(pam.penalties)         ,2)     AS penalties
     , ROUND(AVG(pam.dribbling)         ,2)     AS dribbling
     , ROUND(AVG(pam.short_passing)     ,2)     AS short_passing     
     , ROUND(AVG(pam.long_passing)      ,2)     AS long_passing
     , ROUND(AVG(pam.long_shots)        ,2)     AS long_shots
     , ROUND(AVG(pam.interceptions)     ,2)     AS interceptions
     , ROUND(AVG(pam.marking)           ,2)     AS marking
     , ROUND(AVG(pam.ball_control)      ,2)     AS ball_control
     , ROUND(AVG(pam.heading_accuracy)  ,2)     AS heading_accuracy
     , ROUND(AVG(pam.acceleration)		,2)     AS acceleration
    FROM Player_Attributes_Modified     pam
    JOIN Tb_Total                       tbt
	WHERE pam.date = (SELECT MAX(date)
						FROM Player_Attributes_Modified pam2
					  WHERE pam2.player_api_id = pam.player_api_id
					 )
    GROUP BY pam.preferred_foot ;
 