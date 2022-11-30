-- =====================================================================================
-- QUESTÃO 2B - Insert na tabela Player_Attributes_Modified
-- Somente dados com Json válido
-- =====================================================================================

-- DELETE FROM Player_Attributes_Modified;
INSERT INTO Player_Attributes_Modified (   id
										 , player_fifa_api_id
										 , player_api_id	
										 , date
										 , overall_rating
										 , potential		
										 , preferred_foot
										 , attacking_work_rate
										 , defensive_work_rate
										 , crossing		
										 , finishing
										 , heading_accuracy
										 , short_passing
										 , volleys
										 , dribbling
										 , curve
										 , free_kick_accuracy
										 , long_passing 
										 , ball_control 
										 , acceleration 
										 , sprint_speed 
										 , agility
										 , reactions
										 , balance
										 , shot_power 
										 , jumping
										 , stamina
										 , strength 
										 , long_shots 
										 , aggression 
										 , interceptions
										 , positioning
										 , vision 
										 , penalties
										 , marking
										 , standing_tackle
										 , sliding_tackle 
										 , gk_diving
										 , gk_handling
										 , gk_kicking 
										 , gk_positioning 
										 , gk_reflexes
	 )
  SELECT  JSON_EXTRACT(pa.Player_Attributes, '$.id') 					AS	id
		 ,JSON_EXTRACT(pa.Player_Attributes, '$.player_fifa_api_id')	AS  player_fifa_api_id
		 ,JSON_EXTRACT(pa.Player_Attributes, '$.player_api_id')			AS  player_api_id	
		 ,JSON_EXTRACT(pa.Player_Attributes, '$.date')					AS date
		 ,JSON_EXTRACT(pa.Player_Attributes, '$.overall_rating')		AS overall_rating
		 ,JSON_EXTRACT(pa.Player_Attributes, '$.potential')				AS potential		
		 ,JSON_EXTRACT(pa.Player_Attributes, '$.preferred_foot')		AS preferred_foot
		 ,JSON_EXTRACT(pa.Player_Attributes, '$.attacking_work_rate')	AS attacking_work_rat
		 ,JSON_EXTRACT(pa.Player_Attributes, '$.defensive_work_rate')	AS defensive_work_rat
		 ,JSON_EXTRACT(pa.Player_Attributes, '$.crossing')				AS  crossing		
		 ,JSON_EXTRACT(pa.Player_Attributes, '$.finishing')				AS  finishing
		 ,JSON_EXTRACT(pa.Player_Attributes, '$.heading_accuracy')		AS  heading_accuracy
		 ,JSON_EXTRACT(pa.Player_Attributes, '$.short_passing')			AS  short_passing
		 ,JSON_EXTRACT(pa.Player_Attributes, '$.volleys')				AS  volleys
		 ,JSON_EXTRACT(pa.Player_Attributes, '$.dribbling')				AS  dribbling
		 ,JSON_EXTRACT(pa.Player_Attributes, '$.curve')					AS  curve
		 ,JSON_EXTRACT(pa.Player_Attributes, '$.free_kick_accuracy')	AS  free_kick_accuracy
		 ,JSON_EXTRACT(pa.Player_Attributes, '$.long_passing')			AS  long_passing 
		 ,JSON_EXTRACT(pa.Player_Attributes, '$.ball_control')			AS  ball_control 
		 ,JSON_EXTRACT(pa.Player_Attributes, '$.acceleration')			AS  acceleration 
		 ,JSON_EXTRACT(pa.Player_Attributes, '$.sprint_speed')			AS  sprint_speed 
		 ,JSON_EXTRACT(pa.Player_Attributes, '$.agility')				AS  agility
		 ,JSON_EXTRACT(pa.Player_Attributes, '$.reactions')				AS  reactions
		 ,JSON_EXTRACT(pa.Player_Attributes, '$.balance')				AS  balance
		 ,JSON_EXTRACT(pa.Player_Attributes, '$.shot_power')			AS  shot_power 
		 ,JSON_EXTRACT(pa.Player_Attributes, '$.jumping')				AS  jumping
		 ,JSON_EXTRACT(pa.Player_Attributes, '$.stamina')				AS  stamina
		 ,JSON_EXTRACT(pa.Player_Attributes, '$.strength')				AS  strength 
		 ,JSON_EXTRACT(pa.Player_Attributes, '$.long_shots')			AS  long_shots 
		 ,JSON_EXTRACT(pa.Player_Attributes, '$.aggression')			AS  aggression 
		 ,JSON_EXTRACT(pa.Player_Attributes, '$.interceptions')			AS  interceptions
		 ,JSON_EXTRACT(pa.Player_Attributes, '$.positioning')			AS  positioning
		 ,JSON_EXTRACT(pa.Player_Attributes, '$.vision')				AS  vision 
		 ,JSON_EXTRACT(pa.Player_Attributes, '$.penalties')				AS  penalties
		 ,JSON_EXTRACT(pa.Player_Attributes, '$.marking')				AS  marking
		 ,JSON_EXTRACT(pa.Player_Attributes, '$.standing_tackle')		AS  standing_tackle
		 ,JSON_EXTRACT(pa.Player_Attributes, '$.sliding_tackle')		AS  sliding_tackle 
		 ,JSON_EXTRACT(pa.Player_Attributes, '$.gk_diving')				AS  gk_diving
		 ,JSON_EXTRACT(pa.Player_Attributes, '$.gk_handling')			AS  gk_handling
		 ,JSON_EXTRACT(pa.Player_Attributes, '$.gk_kicking')			AS  gk_kicking 
		 ,JSON_EXTRACT(pa.Player_Attributes, '$.gk_positioning')		AS  gk_positioning 
		 ,JSON_EXTRACT(pa.Player_Attributes, '$.gk_reflexes')			AS  gk_reflexes
	FROM Player_Attributes	pa
	JOIN Player				p 	ON p.player_api_id = JSON_EXTRACT(pa.Player_Attributes,'$.player_api_id') 
	WHERE JSON_VALID(pa.Player_Attributes) = 1
	--AND p.player_api_id = 505942