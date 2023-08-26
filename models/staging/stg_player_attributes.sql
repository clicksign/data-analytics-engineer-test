SELECT CAST(player_attributes AS text) AS player_attributes
FROM {{ source('Fifadata','Player_Attributes') }}
