SELECT
    CAST(id AS integer) AS id,
    CAST(team_api_id AS integer) AS team_api_id,
    CAST(team_fifa_api_id AS integer) AS team_fifa_api_id,
    CAST(team_long_name AS text) AS team_long_name,
    CAST(team_short_name AS text) AS team_short_name
FROM {{ source('Fifadata','Team') }}
