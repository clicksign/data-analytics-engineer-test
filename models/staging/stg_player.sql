SELECT
    CAST(id AS integer) AS id,
    CAST(player_api_id AS integer) AS player_api_id,
    CAST(player_name AS text) AS player_name,
    CAST(player_fifa_api_id AS integer) AS player_fifa_api_id,
    DATE(CAST(birthday AS text)) AS birthday,
    CAST(height AS real) AS height,
    CAST(weight AS integer) AS weight
FROM {{ source('Fifadata','Player') }}
