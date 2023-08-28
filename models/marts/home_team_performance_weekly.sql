WITH match AS ( -- noqa: PRS
    SELECT
        home_team_api_id AS team_id,
        date,
        home_team_goal
    FROM {{ ref('stg_match') }}
)
,
teams AS (
    SELECT
        team_api_id AS team_id,
        team_long_name
    FROM {{ ref('stg_team') }}
)
,
base AS (
    SELECT
        match.team_id,
        match.date,
        match.home_team_goal,
        teams.team_long_name
    FROM match
    left join teams on match.team_id = teams.team_id
)

SELECT
    team_id,
    team_long_name AS team_name,
    strftime('%Y-%m-%d', week_start) AS week_start,
    SUM(home_team_goal) AS weekly_home_goals
FROM (
    SELECT
        team_id,
        date,
        home_team_goal,
        team_long_name,
        date(date, '-6 days', 'weekday 0') AS week_start
    FROM base
)
GROUP BY
    team_id, week_start
-- eu entregaria mais métricas, mas o web scraping da fonte de dados está com problemas para trazer informações sobre:
--'goal',
--'shoton',
--'shotoff',
--'card',
--'foulcommit',
--'cross',
--'corner',
--'possession',
-- que entrariam facilmente no sql acima.
