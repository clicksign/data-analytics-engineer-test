{%- set team_attributes_columns_by_type = {
    'date': ['date'],
    'text': ['buildUpPlaySpeedClass',
               'buildUpPlayDribblingClass',
               'buildUpPlayPassingClass',
               'buildUpPlayPositioningClass',
               'chanceCreationPassingClass',
               'chanceCreationCrossingClass',
               'chanceCreationShootingClass',
               'chanceCreationPositioningClass',
               'defencePressureClass',
               'defenceAggressionClass',
               'defenceTeamWidthClass',
               'defenceDefenderLineClass'],
    'integer': ['id',
                'team_fifa_api_id',
                'team_api_id',
                'buildUpPlaySpeed',
                'buildUpPlayDribbling',
                'buildUpPlayPassing',
                'chanceCreationPassing',
                'chanceCreationCrossing',
                'chanceCreationShooting',
                'defencePressure',
                'defenceAggression',
                'defenceTeamWidth']
} %}

{%- set team_attributes_columns = team_attributes_columns_by_type['date'] +
                                  team_attributes_columns_by_type['integer'] +
                                  team_attributes_columns_by_type['text']
%}

WITH team_attributes AS (
    SELECT
        {%- for _column in team_attributes_columns_by_type['integer'] %}
        CAST(JSON_EXTRACT(team_attributes, '$.{{ _column }}') AS integer) AS {{ _column }},
        {%- endfor %}
        {%- for _column in team_attributes_columns_by_type['text'] %}
        CAST(JSON_EXTRACT(team_attributes, '$.{{ _column }}') AS text) AS {{ _column }},
        {%- endfor %}
        {%- for _column in team_attributes_columns_by_type['date'] %}
        DATE(CAST(JSON_EXTRACT(team_attributes, '$.{{ _column }}') AS text)) AS {{ _column }}{{ ',' if not loop.last }}
        {%- endfor %}
    FROM {{ source('Fifadata','Team_Attributes') }}
)

SELECT
    team_fifa_api_id AS unique_field,
    COUNT(DISTINCT team_api_id) AS distinct_team_api_id_count

FROM team_attributes
WHERE team_fifa_api_id IS NOT NULL
GROUP BY team_fifa_api_id
HAVING distinct_team_api_id_count > 1
