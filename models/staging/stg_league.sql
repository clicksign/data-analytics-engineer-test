SELECT
    id,
    country_id,
    name
FROM {{ source('Fifadata','League') }}
