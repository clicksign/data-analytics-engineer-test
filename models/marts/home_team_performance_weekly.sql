WITH match AS ( -- noqa: PRS
    SELECT
        home_team_api_id AS team_id,
        date,
        home_team_goal,
        away_team_goal
    FROM {{ ref('stg_match') }}
),
teams AS (
    SELECT
        team_api_id AS team_id,
        team_long_name
    FROM {{ ref('stg_team') }}
),
base AS (
    SELECT
        match.team_id,
        match.date,
        match.home_team_goal,
        match.away_team_goal,
        teams.team_long_name
    FROM match
    LEFT JOIN teams ON match.team_id = teams.team_id
)

SELECT
    team_id,
    team_long_name AS team_name,
    strftime('%Y-%m-%d', week_start) AS week_start,
    SUM(home_team_goal) AS weekly_home_goals,
    SUM(away_team_goal) AS weekly_away_goals,
    SUM(home_team_goal + away_team_goal) AS total_weekly_goals,
    COUNT(*) AS total_weekly_matches,
    SUM(home_team_goal + away_team_goal) - SUM(away_team_goal) AS goal_difference,
    AVG(home_team_goal + away_team_goal) AS average_weekly_goals,
    SUM(CASE WHEN home_team_goal > away_team_goal THEN 1 ELSE 0 END) +
    SUM(CASE WHEN away_team_goal > home_team_goal THEN 1 ELSE 0 END) AS weekly_wins,
    SUM(CASE WHEN home_team_goal = away_team_goal THEN 1 ELSE 0 END) AS weekly_draws,
    SUM(CASE WHEN home_team_goal < away_team_goal THEN 1 ELSE 0 END) +
    SUM(CASE WHEN away_team_goal < home_team_goal THEN 1 ELSE 0 END) AS weekly_losses,
    ((SUM(CASE WHEN home_team_goal > away_team_goal THEN 1 ELSE 0 END) +
    SUM(CASE WHEN away_team_goal > home_team_goal THEN 1 ELSE 0 END)) /
    COUNT(*)) AS weekly_win_rate
FROM (
    SELECT
        team_id,
        date,
        home_team_goal,
        away_team_goal,
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
