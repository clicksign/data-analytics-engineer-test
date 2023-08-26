SELECT
    CAST(id AS integer) AS id,
    CAST(country_id AS integer) AS country_id,
    CAST(name AS text) AS name
FROM {{ source('Fifadata','League') }}
