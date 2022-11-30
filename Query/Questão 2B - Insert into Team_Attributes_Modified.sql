-- =====================================================================================
-- QUESTÃO 2B - Insert na tabela Team_Attributes_Modified
-- Somente dados com Json válido
-- =====================================================================================

-- DELETE FROM Team_Attributes_Modified;
INSERT INTO Team_Attributes_Modified (    id
                                        , team_fifa_api_id
                                        , team_api_id	
                                        , date
                                        , buildUpPlaySpeed
                                        , buildUpPlaySpeedClass			
                                        , buildUpPlayDribbling			
                                        , buildUpPlayDribblingClass		
                                        , buildUpPlayPassing			
                                        , buildUpPlayPassingClass		
                                        , buildUpPlayPositioningClass	
                                        , chanceCreationPassing			
                                        , chanceCreationPassingClass	
                                        , chanceCreationCrossing		
                                        , chanceCreationCrossingClass	
                                        , chanceCreationShooting		
                                        , chanceCreationShootingClass	
                                        , chanceCreationPositioningClass
                                        , defencePressure
                                        , defencePressureClass			
                                        , defenceAggression
                                        , defenceAggressionClass		
                                        , defenceTeamWidth
                                        , defenceTeamWidthClass			
                                        , defenceDefenderLineClass		
										)
  SELECT  JSON_EXTRACT(ta.Team_Attributes, '$.id')								AS	id
		 ,JSON_EXTRACT(ta.Team_Attributes, '$.team_fifa_api_id')				AS  team_fifa_api_id
		 ,JSON_EXTRACT(ta.Team_Attributes, '$.team_api_id')						AS  team_api_id	
		 ,JSON_EXTRACT(ta.Team_Attributes, '$.date')							AS  date
		 ,JSON_EXTRACT(ta.Team_Attributes, '$.buildUpPlaySpeed')				AS  buildUpPlaySpeed
		 ,JSON_EXTRACT(ta.Team_Attributes, '$.buildUpPlaySpeedClass')			AS  buildUpPlaySpeedClass			
		 ,JSON_EXTRACT(ta.Team_Attributes, '$.buildUpPlayDribbling')			AS  buildUpPlayDribbling			
		 ,JSON_EXTRACT(ta.Team_Attributes, '$.buildUpPlayDribblingClass')		AS  buildUpPlayDribblingClass		
		 ,JSON_EXTRACT(ta.Team_Attributes, '$.buildUpPlayPassing')				AS  buildUpPlayPassing			
		 ,JSON_EXTRACT(ta.Team_Attributes, '$.buildUpPlayPassingClass')			AS  buildUpPlayPassingClass		
		 ,JSON_EXTRACT(ta.Team_Attributes, '$.buildUpPlayPositioningClass')		AS  buildUpPlayPositioningClass	
		 ,JSON_EXTRACT(ta.Team_Attributes, '$.chanceCreationPassing')			AS  chanceCreationPassing			
		 ,JSON_EXTRACT(ta.Team_Attributes, '$.chanceCreationPassingClass')		AS  chanceCreationPassingClass	
		 ,JSON_EXTRACT(ta.Team_Attributes, '$.chanceCreationCrossing')			AS  chanceCreationCrossing		
		 ,JSON_EXTRACT(ta.Team_Attributes, '$.chanceCreationCrossingClass')		AS  chanceCreationCrossingClass	
		 ,JSON_EXTRACT(ta.Team_Attributes, '$.chanceCreationShooting')			AS  chanceCreationShooting		
		 ,JSON_EXTRACT(ta.Team_Attributes, '$.chanceCreationShootingClass')		AS  chanceCreationShootingClass	
		 ,JSON_EXTRACT(ta.Team_Attributes, '$.chanceCreationPositioningClass')	AS  chanceCreationPositioningClass
		 ,JSON_EXTRACT(ta.Team_Attributes, '$.defencePressure')					AS  defencePressure
		 ,JSON_EXTRACT(ta.Team_Attributes, '$.defencePressureClass')			AS  defencePressureClass			
		 ,JSON_EXTRACT(ta.Team_Attributes, '$.defenceAggression')				AS  defenceAggression
		 ,JSON_EXTRACT(ta.Team_Attributes, '$.defenceAggressionClass')			AS  defenceAggressionClass		
		 ,JSON_EXTRACT(ta.Team_Attributes, '$.defenceTeamWidth')				AS  defenceTeamWidth
		 ,JSON_EXTRACT(ta.Team_Attributes, '$.defenceTeamWidthClass')			AS  defenceTeamWidthClass			
		 ,JSON_EXTRACT(ta.Team_Attributes, '$.defenceDefenderLineClass')		AS  defenceDefenderLineClass		
	FROM Team_Attributes	ta
	JOIN Team 				t	ON t.team_api_id = JSON_EXTRACT(ta.Team_Attributes,'$.team_api_id') 
	WHERE JSON_VALID(ta.Team_Attributes) = 1
	-- AND t.team_api_id = 9930