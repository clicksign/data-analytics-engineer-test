/**Questão 5 - Utiize SQL-CTE**/


/*Semanalmente o gerente da Fifa solicita a média de gols dos times mandantes,
porém como você gosta de entregar mais do que lhe pedem, você resolveu montar uma 
CTE para entregar outras métricas para seu gerente. Como você faria, em SQL,
para salvar ou automatizar essa query? Envie-nos seu código.*/


-- SQLite
-- Seleciona id e nome do time 
with Teams as (
    SELECT 
        team_api_id
        , team_long_name       
    FROM Team
)

-- Realiza soma e media de gols por time e por temporada em casa
, goals_home as (
    SELECT
        home_team_api_id
        , sum(home_team_goal) as sum_home_goals 
        , avg(home_team_goal) as average_home_gols
        , season
    FROM Match
    GROUP BY
        home_team_api_id
        , season
) 

-- Realiza soma e media de gols por time e por temporada fora de casa
, goals_away as (
    SELECT
        away_team_api_id
        , sum(away_team_goal) as sum_away_goals
        , avg(away_team_goal) as average_away_gols
        , season
    FROM Match
    GROUP BY
        away_team_api_id
        , season
        
) 

--Realiza o join das somas acima e mostra os dados unificados.
, joined as (
    SELECT
       team_api_id
        , team_long_name
        , sum_home_goals
        , sum_away_goals
        , average_home_gols
        , average_away_gols
        , goals_home.season
    FROM Teams
    LEFT JOIN goals_home
        ON Teams.team_api_id = goals_home.home_team_api_id
    LEFT JOIN goals_away
        ON goals_home.home_team_api_id = goals_away.away_team_api_id
        and  goals_home.season = goals_away.season
) 

SELECT * FROM joined order by 3 desc, 2, 7
