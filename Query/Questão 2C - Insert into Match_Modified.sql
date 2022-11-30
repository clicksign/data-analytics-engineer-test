-- =====================================================================================
-- QUESTÃO 2C - Insert na tabela Match_Modified no formato JSON
-- =====================================================================================

-- DELETE FROM Match_Modified;
INSERT INTO Match_Modified (id, Match_Modified)
	SELECT   id,
			 JSON('{'						||
				  '"id":"' 					|| id 				|| '",' || 
				  '"match_api_id":"' 		|| match_api_id 	|| '",' ||
				  '"home_team_api_id":"' 	|| home_team_api_id || '",' ||
				  '"away_team_api_id":"' 	|| away_team_api_id || '"' 	||        
				  '}') AS Match_Modified
	 FROM Match ;

/* 
	SELECT JSON_EXTRACT(Match_Modified, '$.home_team_api_id') AS home_team_api_id  
		FROM Match_Modified;
*/