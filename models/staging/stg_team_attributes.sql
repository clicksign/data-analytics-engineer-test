SELECT team_attributes
FROM {{ source('Fifadata','Team_Attributes') }}
