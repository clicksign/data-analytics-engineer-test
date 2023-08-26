SELECT
    JSON_OBJECT(
        'id', id,
        'match_api_id', match_api_id,
        'home_team_api_id', home_team_api_id,
        'away_team_api_id', away_team_api_id
    ) AS match_modified
FROM {{ ref('stg_match') }}
