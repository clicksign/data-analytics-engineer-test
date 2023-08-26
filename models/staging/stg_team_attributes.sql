SELECT CAST(team_attributes AS text) AS team_attributes
FROM {{ source('Fifadata','Team_Attributes') }}
