SELECT
    'Home' AS team_type,
    ROUND(SUM(CASE WHEN home_team_goal > away_team_goal THEN 1 ELSE 0 END) * 100 / COUNT(*), 2) AS win_percentage
FROM {{ ref('stg_match') }}
UNION ALL
SELECT
    'Away' AS team_type,
    ROUND(SUM(CASE WHEN away_team_goal > home_team_goal THEN 1 ELSE 0 END) * 100 / COUNT(*), 2) AS win_percentage
FROM {{ ref('stg_match') }}
