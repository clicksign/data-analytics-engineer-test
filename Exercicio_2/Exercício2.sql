-- SQLite
--Estabeleça uma relação entre as tabelas **Player** e  **Player_Attributes** em uma nova tabela, chamada **‘Player_Attributes_Modified’**, onde cada key do json é uma nova coluna
-- Foi necessário realizar um tratamento nas colunas abaixo que estavam vindo com caracteres de texto onde deveriam ser números, impedindo o tratamento de extração do json
create table Player_Attributes_Modified as
SELECT
    Player.id as id_player 
    ,Player.player_api_id
    ,Player.player_name
    ,Player.player_fifa_api_id
    ,Player.birthday
    ,Player.height
    ,Player.weight
    ,json_extract(replace(Player_Attributes,'NaN',0),'$.id') as id_attribute
    ,json_extract(replace(Player_Attributes,'NaN',0),'$.date') as date
    ,json_extract(replace(Player_Attributes,'NaN',0),'$.overall_rating') as overall_rating
    ,json_extract(replace(Player_Attributes,'NaN',0),'$.potential') as potential
    ,json_extract(replace(Player_Attributes,'NaN',0),'$.preferred_foot') as preferred_foot
    ,json_extract(replace(Player_Attributes,'NaN',0),'$.attacking_work_rate') as attacking_work_rate
    ,json_extract(replace(Player_Attributes,'NaN',0),'$.defensive_work_rate') as defensive_work_rate
    ,json_extract(replace(Player_Attributes,'NaN',0),'$.crossing') as crossing
    ,json_extract(replace(Player_Attributes,'NaN',0),'$.finishing') as finishing
    ,json_extract(replace(Player_Attributes,'NaN',0),'$.heading_accuracy') as heading_accuracy
    ,json_extract(replace(Player_Attributes,'NaN',0),'$.short_passing') as short_passing
    ,json_extract(replace(Player_Attributes,'NaN',0),'$.volleys') as volleys
    ,json_extract(replace(Player_Attributes,'NaN',0),'$.dribbling') as dribbling
    ,json_extract(replace(Player_Attributes,'NaN',0),'$.curve') as curve
    ,json_extract(replace(Player_Attributes,'NaN',0),'$.free_kick_accuracy') as free_kick_accuracy
    ,json_extract(replace(Player_Attributes,'NaN',0),'$.long_passing') as long_passing
    ,json_extract(replace(Player_Attributes,'NaN',0),'$.ball_control') as ball_control
    ,json_extract(replace(Player_Attributes,'NaN',0),'$.acceleration') as acceleration
    ,json_extract(replace(Player_Attributes,'NaN',0),'$.sprint_speed') as sprint_speed
    ,json_extract(replace(Player_Attributes,'NaN',0),'$.agility') as agility
    ,json_extract(replace(Player_Attributes,'NaN',0),'$.reactions') as reactions
    ,json_extract(replace(Player_Attributes,'NaN',0),'$.balance') as balance
    ,json_extract(replace(Player_Attributes,'NaN',0),'$.shot_power') as shot_power
    ,json_extract(replace(Player_Attributes,'NaN',0),'$.jumping') as jumping
    ,json_extract(replace(Player_Attributes,'NaN',0),'$.stamina') as stamina
    ,json_extract(replace(Player_Attributes,'NaN',0),'$.strength') as strength
    ,json_extract(replace(Player_Attributes,'NaN',0),'$.long_shots') as long_shots
    ,json_extract(replace(Player_Attributes,'NaN',0),'$.aggression') as aggression
    ,json_extract(replace(Player_Attributes,'NaN',0),'$.interceptions') as interceptions
    ,json_extract(replace(Player_Attributes,'NaN',0),'$.positioning') as positioning
    ,json_extract(replace(Player_Attributes,'NaN',0),'$.vision') as vision
    ,json_extract(replace(Player_Attributes,'NaN',0),'$.penalties') as penalties
    ,json_extract(replace(Player_Attributes,'NaN',0),'$.marking') as marking
    ,json_extract(replace(Player_Attributes,'NaN',0),'$.standing_tackle') as standing_tackle
    ,json_extract(replace(Player_Attributes,'NaN',0),'$.sliding_tackle') as sliding_tackle
    ,json_extract(replace(Player_Attributes,'NaN',0),'$.gk_diving') as gk_diving
    ,json_extract(replace(Player_Attributes,'NaN',0),'$.gk_handling') as gk_handling
    ,json_extract(replace(Player_Attributes,'NaN',0),'$.gk_kicking') as gk_kicking
    ,json_extract(replace(Player_Attributes,'NaN',0),'$.gk_positioning') as gk_positioning
    ,json_extract(replace(Player_Attributes,'NaN',0),'$.gk_reflexes') as gk_reflexes  
FROM Player_Attributes
LEFT JOIN Player
    ON json_extract(replace(Player_Attributes,'NaN',0),'$.player_fifa_api_id') = Player.player_fifa_api_id



-- Faça o mesmo para a relação **Team** e **Team_Attributes**, como o nome para a tabela **‘Team_Attributes_Modified’**
-- Foi necessário realizar um tratamento nas colunas abaixo que estavam vindo com caracteres de texto onde deveriam ser números, impedindo o tratamento de extração do json
CREATE TABLE Team_Attributes_Modified AS
SELECT 
    Team.id
    ,Team.team_api_id
    ,Team.team_fifa_api_id
    ,Team.team_long_name
    ,Team.team_short_name
    ,json_extract(replace(Team_Attributes,'NaN',0), '$.id') as id_attribute
    ,json_extract(replace(Team_Attributes,'NaN',0), '$.date') as date
    ,json_extract(replace(Team_Attributes,'NaN',0), '$.buildUpPlaySpeed') as buildUpPlaySpeed
    ,json_extract(replace(Team_Attributes,'NaN',0), '$.buildUpPlaySpeedClass') as buildUpPlaySpeedClass
    ,json_extract(replace(Team_Attributes,'NaN',0), '$.buildUpPlayDribbling') as buildUpPlayDribbling
    ,json_extract(replace(Team_Attributes,'NaN',0), '$.buildUpPlayDribblingClass') as buildUpPlayDribblingClass
    ,json_extract(replace(Team_Attributes,'NaN',0), '$.buildUpPlayPassing') as buildUpPlayPassing
    ,json_extract(replace(Team_Attributes,'NaN',0), '$.buildUpPlayPassingClass') as buildUpPlayPassingClass
    ,json_extract(replace(Team_Attributes,'NaN',0), '$.buildUpPlayPositioningClass') as buildUpPlayPositioningClass
    ,json_extract(replace(Team_Attributes,'NaN',0), '$.chanceCreationPassing') as chanceCreationPassing
    ,json_extract(replace(Team_Attributes,'NaN',0), '$.chanceCreationPassingClass') as chanceCreationPassingClass
    ,json_extract(replace(Team_Attributes,'NaN',0), '$.chanceCreationCrossing') as chanceCreationCrossing
    ,json_extract(replace(Team_Attributes,'NaN',0), '$.chanceCreationCrossingClass') as chanceCreationCrossingClass
    ,json_extract(replace(Team_Attributes,'NaN',0), '$.chanceCreationShooting') as chanceCreationShooting
    ,json_extract(replace(Team_Attributes,'NaN',0), '$.chanceCreationShootingClass') as chanceCreationShootingClass
    ,json_extract(replace(Team_Attributes,'NaN',0), '$.chanceCreationPositioningClass') as chanceCreationPositioningClass
    ,json_extract(replace(Team_Attributes,'NaN',0), '$.defencePressure') as defencePressure
    ,json_extract(replace(Team_Attributes,'NaN',0), '$.defencePressureClass') as defencePressureClass
    ,json_extract(replace(Team_Attributes,'NaN',0), '$.defenceAggression') as defenceAggression
    ,json_extract(replace(Team_Attributes,'NaN',0), '$.defenceAggressionClass') as defenceAggressionClass
    ,json_extract(replace(Team_Attributes,'NaN',0), '$.defenceTeamWidth') as defenceTeamWidth
    ,json_extract(replace(Team_Attributes,'NaN',0), '$.defenceTeamWidthClass') as defenceTeamWidthClass
    ,json_extract(replace(Team_Attributes,'NaN',0), '$.defenceDefenderLineClass') as defenceDefenderLineClass
FROM Team_Attributes
LEFT JOIN Team
    ON Team.team_fifa_api_id =  json_extract(replace(Team_Attributes,'NaN',0), '$.team_fifa_api_id')


--Crie uma tabela chamada **Match_Modified** cuja coluna seja representada como JSON, onde as chaves precisam ser referentes às colunas da tabela Match, sendo elas : **id,match_api_id, home_team_api_id, away_team_api_id .**
CREATE TABLE Match_Modified AS 
select    
    ROW_NUMBER() OVER ( order by id) - 1 as id --Para deixar o primeiro registro começando com 0 quando armazenado.
    , json_object(
                'id', cast(id as TEXT)
                ,'match_api_id' , cast(match_api_id as TEXT)
                ,'home_team_api_id', cast(home_team_api_id as TEXT)
                ,'away_team_api_id', cast(away_team_api_id as TEXT)
                ) 
     AS json_column
from Match