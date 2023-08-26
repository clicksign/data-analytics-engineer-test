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

{%- set player_attributes_columns = player_attributes_columns_by_type['integer'] +
                                    player_attributes_columns_by_type['text'] +
                                    player_attributes_columns_by_type['date']
%}

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
    FROM {{ ref('stg_player_attributes') }}
)
,
player AS (
    SELECT
        player_api_id,
        player_name,
        player_fifa_api_id,
        birthday,
        height,
        weight
    FROM {{ ref('stg_player') }}
)

SELECT
    player.player_name,
    player.birthday,
    player.height,
    player.weight,
    {%- for _column in player_attributes_columns %}
    player_attributes.{{ _column }}{{ ',' if not loop.last }}
    {%- endfor %}
FROM player_attributes
    INNER JOIN player ON player_attributes.player_api_id = player.player_api_id
