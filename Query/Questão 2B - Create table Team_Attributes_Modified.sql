-- =====================================================================================
-- QUESTÃO 2B - Criação da tabela Team_Attributes_Modified
-- =====================================================================================

-- DROP TABLE IF EXISTS Team_Attributes_Modified;
CREATE TABLE Team_Attributes_Modified (
	  id								INT
	, team_fifa_api_id					INT
	, team_api_id						INT
	, date								DATETIME
	, buildUpPlaySpeed					FLOAT
	, buildUpPlaySpeedClass				VARCHAR(30)
	, buildUpPlayDribbling				FLOAT
	, buildUpPlayDribblingClass			VARCHAR(30)
	, buildUpPlayPassing				FLOAT
	, buildUpPlayPassingClass			VARCHAR(30)
	, buildUpPlayPositioningClass		VARCHAR(30)
	, chanceCreationPassing				FLOAT
	, chanceCreationPassingClass		VARCHAR(30)
	, chanceCreationCrossing			FLOAT
	, chanceCreationCrossingClass		VARCHAR(30)
	, chanceCreationShooting			FLOAT
	, chanceCreationShootingClass		VARCHAR(30)
	, chanceCreationPositioningClass	VARCHAR(30)	
	, defencePressure					FLOAT
	, defencePressureClass				VARCHAR(30)
	, defenceAggression					FLOAT
	, defenceAggressionClass			VARCHAR(30)
	, defenceTeamWidth					FLOAT
	, defenceTeamWidthClass				VARCHAR(30)
	, defenceDefenderLineClass			VARCHAR(30)
	, PRIMARY KEY (id)
	);