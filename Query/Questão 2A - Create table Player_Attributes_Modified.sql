-- =====================================================================================
-- QUESTÃO 2B - Criação da tabela Player_Attributes_Modified
-- Cria tabela e índice para posterior pesquisa
-- =====================================================================================

-- DROP TABLE IF EXISTS Player_Attributes_Modified;
CREATE TABLE Player_Attributes_Modified (
	  id						INT
	, player_fifa_api_id		INT
	, player_api_id				INT
	, date						DATETIME
	, overall_rating			FLOAT
	, potential					FLOAT
	, preferred_foot			VARCHAR(20)
	, attacking_work_rate		VARCHAR(20)
	, defensive_work_rate		VARCHAR(20)
	, crossing					FLOAT
	, finishing                 FLOAT
	, heading_accuracy          FLOAT
	, short_passing             FLOAT
	, volleys                   FLOAT
	, dribbling                 FLOAT
	, curve                     FLOAT
	, free_kick_accuracy        FLOAT
	, long_passing              FLOAT
	, ball_control              FLOAT
	, acceleration              FLOAT
	, sprint_speed              FLOAT
	, agility                   FLOAT
	, reactions                 FLOAT
	, balance                   FLOAT
	, shot_power                FLOAT
	, jumping                   FLOAT
	, stamina                   FLOAT
	, strength                  FLOAT
	, long_shots                FLOAT
	, aggression                FLOAT
	, interceptions             FLOAT
	, positioning               FLOAT
	, vision                    FLOAT
	, penalties                 FLOAT
	, marking                   FLOAT
	, standing_tackle           FLOAT
	, sliding_tackle            FLOAT
	, gk_diving                 FLOAT
	, gk_handling               FLOAT
	, gk_kicking                FLOAT
	, gk_positioning            FLOAT
	, gk_reflexes               FLOAT
	);
	
--Cria índice para as queries da Questao 3
CREATE INDEX idx_player_attributes_modified_date_player_api_id 
	ON Player_Attributes_Modified (	player_api_id,
									date
);
	