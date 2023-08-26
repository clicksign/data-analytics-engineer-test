WITH unique_id_country AS (
    SELECT
        COALESCE(id, 0) AS not_null_id,
        CASE
            WHEN name IS NULL OR name = '' THEN 'Unknown'
            WHEN name = 'Arábia Saudita' THEN 'Saudi Arabia'
            WHEN name = 'Austrália' THEN 'Australia'
            WHEN name = 'Bélgica' THEN 'Belgium'
            WHEN name = 'Inglaterra' THEN 'England'
            WHEN name = 'França' THEN 'France'
            WHEN name = 'Alemanha' THEN 'Germany'
            WHEN name = 'Itália' THEN 'Italy'
            ELSE name
        END AS name
    FROM {{ source('Fifadata','Country') }}
    GROUP BY not_null_id
)

SELECT
    CAST(not_null_id AS integer) AS id,
    CAST(name AS text) AS name
FROM unique_id_country
UNION ALL
SELECT
    51220 AS id,
    'Angola' AS name
UNION ALL
SELECT
    44560 AS id,
    'Brazil' AS name
-- the data from above I got from the additional countries from stg_league
-- table as I can't use another source as country table.
