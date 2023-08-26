SELECT
    league.id AS league_id,
    league.country_id,
    league.name AS league_name,
    country.name AS country_name
FROM {{ ref('stg_league') }} AS league
    INNER JOIN {{ ref('stg_country') }} AS country ON league.country_id = country.id
