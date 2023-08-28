SELECT
    c.country_name,
    m.season,
    SUM(m.home_team_goal) AS total_home_goals,
    SUM(m.away_team_goal) AS total_away_goals,
    SUM(m.home_team_goal + m.away_team_goal) AS total_goals
FROM {{ ref('stg_match') }} AS m
    INNER JOIN {{ ref('int_team_added_country_league') }} AS c ON m.home_team_api_id = c.team_api_id OR m.away_team_api_id = c.team_api_id
GROUP BY c.country_name, m.season
ORDER BY m.season DESC, total_goals DESC
