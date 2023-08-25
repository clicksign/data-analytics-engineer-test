SELECT player_attributes
FROM {{ source('Fifadata','Player_Attributes') }}
