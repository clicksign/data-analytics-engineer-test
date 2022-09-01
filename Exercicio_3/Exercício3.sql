-- Qual a proporção entre jogadores destros e canhotos?
SELECT
    count(distinct id_player) as count_players
    , preferred_foot 
FROM Player_Attributes_Modified
where preferred_foot not like '0' -- Retira os que estão sem preenchimento
group by preferred_foot 
-------------------------------------------------------------------------------------------------

-- Quais os nomes dos jogadores e qual o pé que eles chutam?
SELECT
    id_player
    , player_name
    , preferred_foot 
FROM Player_Attributes_Modified
where preferred_foot not like '0' -- Retira os que estão sem preenchimento
group by 
    id_player
    , player_name
    , preferred_foot 

-------------------------------------------------------------------------------------------------

-- Jogadores que chutam com os dois pé
SELECT
    count(distinct preferred_foot) as count_preferred_foot
    , player_name 
FROM Player_Attributes_Modified
where preferred_foot not like '0' -- Retira os que estão sem preenchimento
group by player_name
having count(distinct preferred_foot) > 1 -- Seleciona os jogadores que chutam com mais de 1 pé
order by 2

-------------------------------------------------------------------------------------------------

-- Numero de jogadores que chutam com os dois pés
WITH player_kick as (
    SELECT
        count(distinct preferred_foot) as count_preferred_foot
        , player_name 
    FROM Player_Attributes_Modified
    where preferred_foot not like '0' -- Retira os que estão sem preenchimento
    group by player_name
    having count(distinct preferred_foot) > 1 -- Seleciona os jogadores que chutam com mais de 1 pé
)

SELECT
    count(player_name) as count_player_kick_both_feet
from player_kick
--count_player_kick_both_feet
--1172

-------------------------------------------------------------------------------------------------

-- País com maior número de gols
-- Primeiro select ordera por número do ID do país para separar os país que estão com os nomes em PT e EN.
with country_count as (
    SELECT 
        id
        , name
        , ROW_NUMBER() OVER (PARTITION BY id ORDER BY id) as count_country -- Enumera os países com nome em português e inglÊs
    FROM Country
)


, goals as (
    SELECT
        country_count.id
        , name
        , home_team_goal
        , away_team_goal
    FROM country_count
    LEFT JOIN Match
        ON country_count.id = Match.country_id
    WHERE
        country_count.id is not null -- não nulos
        and country_count.id <> 0 -- diferentes de zero
        and count_country = 1 -- selecionar o primeiro país enumerado acima para não duplicar os dados
) 

-- Seleciona com base na tabela anterior o páis com maior número de gols.
SELECT 
    id
    , name
    , max(number_goals) as max_goals
FROM (SELECT 
            id
            , name
            , sum(home_team_goal+away_team_goal) as number_goals
        FROM goals
       GROUP BY id, name)
-- Resposta: id	    name	max_goals
--          21518	Spain	8412
       
-------------------------------------------------------------------------------------------------
----- Time com mais saldos de Gols-----
with Teams as (
    SELECT 
        team_api_id
        , team_long_name       
    FROM Team
)

--Seleciona os gols em casa
, goals_home as (
    SELECT
        home_team_api_id
        , home_team_goal
    FROM Match
) 
--Seleciona os gols fora de casa
, goals_away as (
    SELECT
        away_team_api_id
        , away_team_goal
    FROM Match
) 

-- Join e soma dos gols por time e nome do time
, team_goals as (
    SELECT
       team_api_id
        , team_long_name
        , SUM(home_team_goal) home_goals
        , SUM(away_team_goal) away_goals
        , SUM(home_team_goal-away_team_goal) goals_dirference 
    FROM Teams
    LEFT JOIN goals_home
        ON Teams.team_api_id = goals_home.home_team_api_id
    LEFT JOIN goals_away
        ON Teams.team_api_id = goals_away.away_team_api_id
    GROUP BY team_api_id
        , team_long_name
) 

SELECT * FROM team_goals
order by 5 desc 
--team_api_id	team_long_name	home_goals	away_goals	goals_dirference
--8633	        Real Madrid CF	76760	        51376	25384
--8634	        FC Barcelona	75240	        53808	21432


-------------------------------------------------------------------------------------------------

----- ID de países que não estão na tabela Country ---
WITH country_count as (
    SELECT 
         id
        , name as country_name
        , ROW_NUMBER() OVER (PARTITION BY id ORDER BY id) as count_country -- Numerrar os países com nome em português e inglÊs
    FROM Country
)

, joined as (
    SELECT 
        Country_id
        , country_name
    FROM League
    LEFT JOIN country_count
        ON League.country_id = country_count.id
    WHERE
        count_country = 1 -- selececionar o primeiro país enumerado acima para não duplicar os dados 
        OR country_count.id IS NULL --  selecionar os ID que não estão na tabela Country
)
SELECT * 
FROM joined
WHERE country_name IS NULL
--Resultou em 2 ID de países que não estão na tabela Country (44560 e 51220)


