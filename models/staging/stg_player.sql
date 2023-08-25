SELECT
    id,
    player_api_id,
    player_name,
    player_fifa_api_id,
    birthday,
    height,
    weight
FROM {{ source('Fifadata','Player') }}
