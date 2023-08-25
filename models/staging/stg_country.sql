SELECT
    id,
    name
FROM {{ source('Fifadata','Country') }}
