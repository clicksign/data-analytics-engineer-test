-- COMMAND LINE: 
-- sqlite3 test_analytics_engineer.db

-- SQLite:

-- Player_Attributes_Modified
-- to get json keys:
SELECT DISTINCT json_each.key FROM Player_Attributes, json_each(Player_Attributes) WHERE json_valid(Player_Attributes);

-- Table creation
CREATE TABLE Player_Attributes_Modified AS
SELECT json_extract(Player_Attributes, '$.id') AS id
, json_extract(Player_Attributes, '$.player_fifa_api_id') AS player_fifa_api_id
, json_extract(Player_Attributes, '$.player_api_id') AS player_api_id
, json_extract(Player_Attributes, '$.date') AS date
, json_extract(Player_Attributes, '$.overall_rating') AS overall_rating
, json_extract(Player_Attributes, '$.potential') AS potential
, json_extract(Player_Attributes, '$.preferred_foot') AS preferred_foot
, json_extract(Player_Attributes, '$.attacking_work_rate') AS attacking_work_rate
, json_extract(Player_Attributes, '$.defensive_work_rate') AS defensive_work_rate
, json_extract(Player_Attributes, '$.crossing') AS crossing
, json_extract(Player_Attributes, '$.finishing') AS finishing
, json_extract(Player_Attributes, '$.heading_accuracy') AS heading_accuracy
, json_extract(Player_Attributes, '$.short_passing') AS short_passing
, json_extract(Player_Attributes, '$.volleys') AS volleys
, json_extract(Player_Attributes, '$.dribbling') AS dribbling
, json_extract(Player_Attributes, '$.curve') AS curve
, json_extract(Player_Attributes, '$.free_kick_accuracy') AS free_kick_accuracy
, json_extract(Player_Attributes, '$.long_passing') AS long_passing
, json_extract(Player_Attributes, '$.ball_control') AS ball_control
, json_extract(Player_Attributes, '$.acceleration') AS acceleration
, json_extract(Player_Attributes, '$.sprint_speed') AS sprint_speed
, json_extract(Player_Attributes, '$.agility') AS agility
, json_extract(Player_Attributes, '$.reactions') AS reactions
, json_extract(Player_Attributes, '$.balance') AS balance
, json_extract(Player_Attributes, '$.shot_power') AS shot_power
, json_extract(Player_Attributes, '$.jumping') AS jumping
, json_extract(Player_Attributes, '$.stamina') AS stamina
, json_extract(Player_Attributes, '$.strength') AS strength
, json_extract(Player_Attributes, '$.long_shots') AS long_shots
, json_extract(Player_Attributes, '$.aggression') AS aggression
, json_extract(Player_Attributes, '$.interceptions') AS interceptions
, json_extract(Player_Attributes, '$.positioning') AS positioning
, json_extract(Player_Attributes, '$.vision') AS vision
, json_extract(Player_Attributes, '$.penalties') AS penalties
, json_extract(Player_Attributes, '$.marking') AS marking
, json_extract(Player_Attributes, '$.standing_tackle') AS standing_tackle
, json_extract(Player_Attributes, '$.sliding_tackle') AS sliding_tackle
, json_extract(Player_Attributes, '$.gk_diving') AS gk_diving
, json_extract(Player_Attributes, '$.gk_handling') AS gk_handling
, json_extract(Player_Attributes, '$.gk_kicking') AS gk_kicking
, json_extract(Player_Attributes, '$.gk_positioning') AS gk_positioning
, json_extract(Player_Attributes, '$.gk_reflexes') AS gk_reflexes
FROM Player_Attributes
        WHERE json_valid(Player_Attributes);

-- Table selection:
SELECT * FROM Player_Attributes_Modified LIMIT 10;


-- Team_Attributes_Modified

-- Table creation:
CREATE TABLE Team_Attributes_Modified AS 
SELECT json_extract(Team_Attributes, '$.id') AS id
, json_extract(Team_Attributes, '$.team_fifa_api_id') AS team_fifa_api_id
, json_extract(Team_Attributes, '$.team_api_id') AS team_api_id
, json_extract(Team_Attributes, '$.date') AS date
, json_extract(Team_Attributes, '$.buildUpPlaySpeed') AS buildUpPlaySpeed
, json_extract(Team_Attributes, '$.buildUpPlaySpeedClass') AS buildUpPlaySpeedClass
, json_extract(Team_Attributes, '$.buildUpPlayDribbling') AS buildUpPlayDribbling
, json_extract(Team_Attributes, '$.buildUpPlayDribblingClass') AS buildUpPlayDribblingClass
, json_extract(Team_Attributes, '$.buildUpPlayPassing') AS buildUpPlayPassing
, json_extract(Team_Attributes, '$.buildUpPlayPassingClass') AS buildUpPlayPassingClass
, json_extract(Team_Attributes, '$.buildUpPlayPositioningClass') AS buildUpPlayPositioningClass
, json_extract(Team_Attributes, '$.chanceCreationPassing') AS chanceCreationPassing
, json_extract(Team_Attributes, '$.chanceCreationPassingClass') AS chanceCreationPassingClass
, json_extract(Team_Attributes, '$.chanceCreationCrossing') AS chanceCreationCrossing
, json_extract(Team_Attributes, '$.chanceCreationCrossingClass') AS chanceCreationCrossingClass
, json_extract(Team_Attributes, '$.chanceCreationShooting') AS chanceCreationShooting
, json_extract(Team_Attributes, '$.chanceCreationShootingClass') AS chanceCreationShootingClass
, json_extract(Team_Attributes, '$.chanceCreationPositioningClass') AS chanceCreationPositioningClass
, json_extract(Team_Attributes, '$.defencePressure') AS defencePressure
, json_extract(Team_Attributes, '$.defencePressureClass') AS defencePressureClass
, json_extract(Team_Attributes, '$.defenceAggression') AS defenceAggression
, json_extract(Team_Attributes, '$.defenceAggressionClass') AS defenceAggressionClass
, json_extract(Team_Attributes, '$.defenceTeamWidth') AS defenceTeamWidth
, json_extract(Team_Attributes, '$.defenceTeamWidthClass') AS defenceTeamWidthClass
, json_extract(Team_Attributes, '$.defenceDefenderLineClass') AS defenceDefenderLineClass
FROM Team_Attributes
    WHERE json_valid(Team_Attributes);

-- Table selection:
SELECT * FROM Team_Attributes_Modified LIMIT 10;

-- Match_Modified

-- Table creation:
CREATE TABLE Match_Modified AS
    SELECT
    json_object(
        'id', id,
        'match_api_id', match_api_id,
        'home_team_api_id', home_team_api_id,
        'away_team_api_id', away_team_api_id
    ) AS Match_Modified
FROM Match;

-- Table selection:
SELECT * FROM Match_Modified LIMIT 10;