SELECT
    team_fifa_api_id AS unique_field,
    COUNT(*) AS n_records
FROM {{ source('Fifadata','Team') }}
WHERE team_fifa_api_id IS NOT NULL
GROUP BY team_fifa_api_id
HAVING COUNT(*) > 1
{# Note that the same unique_field are present in both teams and teams_attributes. #}
