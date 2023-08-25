SELECT
    id,
    team_api_id,
    team_fifa_api_id,
    team_long_name,
    team_short_name
FROM {{ source('Fifadata','Team') }}
