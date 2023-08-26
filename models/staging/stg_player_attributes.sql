{%- set player_attributes_columns_by_type = {
    'date': ['date'],
    'text': ['preferred_foot',
               'attacking_work_rate',
               'defensive_work_rate'],
    'integer': ['id',
                'player_fifa_api_id',
                'player_api_id',
                'overall_rating',
                'potential',
                'crossing',
                'finishing',
                'heading_accuracy',
                'short_passing',
                'volleys',
                'dribbling',
                'curve',
                'free_kick_accuracy',
                'long_passing',
                'ball_control',
                'acceleration',
                'sprint_speed',
                'agility',
                'reactions',
                'balance',
                'shot_power',
                'jumping',
                'stamina',
                'strength',
                'long_shots',
                'aggression',
                'interceptions',
                'positioning',
                'vision',
                'penalties',
                'marking',
                'standing_tackle',
                'sliding_tackle',
                'gk_diving',
                'gk_handling',
                'gk_kicking',
                'gk_positioning',
                'gk_reflexes']
} %}


WITH player_attributes AS (
    SELECT
        {%- for _column in player_attributes_columns_by_type['integer'] %}
        CAST(JSON_EXTRACT(player_attributes, '$.{{ _column }}') AS integer) AS {{ _column }},
        {%- endfor %}
        {%- for _column in player_attributes_columns_by_type['text'] %}
        CAST(JSON_EXTRACT(player_attributes, '$.{{ _column }}') AS text) AS {{ _column }},
        {%- endfor %}
        {%- for _column in player_attributes_columns_by_type['date'] %}
        DATE(CAST(JSON_EXTRACT(player_attributes, '$.{{ _column }}') AS text)) AS {{ _column }}{{ ',' if not loop.last }}
        {%- endfor %}
    FROM {{ source('Fifadata','Player_Attributes') }}
)

SELECT
    CASE WHEN TRIM(preferred_foot) IN ('left', 'right') THEN preferred_foot ELSE 'unknown' END AS preferred_foot,
    CASE WHEN TRIM(attacking_work_rate) IN ('high', 'medium', 'low') THEN attacking_work_rate ELSE 'unknown' END AS attacking_work_rate,
    CASE WHEN TRIM(defensive_work_rate) IN ('high', 'medium', 'low') THEN defensive_work_rate ELSE 'unknown' END AS defensive_work_rate,
    {%- for _column in player_attributes_columns_by_type['date'] %}
    {{ _column }},
    {%- endfor %}
    {%- for _column in player_attributes_columns_by_type['integer'] %}
    {{ _column }}{{ ',' if not loop.last }}
    {%- endfor %}
FROM player_attributes
WHERE
    player_fifa_api_id NOT IN (
        200529,
        197937
    ) -- theses players are missing from the player table and there are no data for them in the player_attributes table
-- they also have a player_api_id that is in the player table with another player_fifa_api_id
-- being 110189,193866. They are in this table and with data.
-- it is probably a mistake in the data and we will ignore them
