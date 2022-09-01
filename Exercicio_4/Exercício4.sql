--Encontre uma relação de dados entre as tabelas League, Country, Team_Attributes e Player, crie uma nova tabela chamada **'Relations'**


CREATE TABLE Relations as
-- Primeiro select ordera por número do ID do país para separar os país que estão com os nomes em PT e EN.
WITH country_count as (
    SELECT 
         id
        , name as country_name
        , ROW_NUMBER() OVER (PARTITION BY id ORDER BY id) as count_country -- Numerrar os países com nome em português e inglês
    FROM Country
)

-- Seleciona apenas os dados de jogadores que jogaram em casa e foram Player_1 na escalação
, home_player as (
    SELECT DISTINCT
        country_id
        , league_id
        , player_api_id
        , player_name
        , home_team_api_id
    FROM Player
    LEFT JOIN Match
        ON player_api_id = home_player_1
)

-- Relaciona as tabelas Countru, League, Home_player, Player e Team_Attributes_Modified 
, joined as (
    SELECT distinct
        League.Country_id
        , country_name
        , League.id as id_league
        , name as league_name
        , league_id
        , home_player.player_api_id
        , home_player.player_name
        , player_fifa_api_id
        , birthday
        , height
        , weight
        , team_api_id
        , team_fifa_api_id
        , team_long_name
        , team_short_name        
    FROM League
    LEFT JOIN country_count
        ON League.country_id = country_count.id 
    LEFT JOIN home_player
        ON league_id = League.id
    LEFT JOIN Player
        ON  Player.player_api_id = home_player.player_api_id
    LEFT JOIN Team_Attributes_Modified
        ON team_api_id = home_team_api_id
    WHERE
        count_country = 1 -- selececionar o primeiro país enumerado acima para não duplicar os dados 
        OR country_count.id IS NULL --  selecionar os ID que não estão na tabela Country
)

select * from joined