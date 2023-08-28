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

WITH team AS (
    SELECT
        id,
        team_api_id,
        team_fifa_api_id,
        team_long_name,
        team_short_name
    FROM {{ source('Fifadata', 'Team') }}
)
,
team_attributes AS (
    SELECT
        {%- for _column in team_attributes_columns_by_type['integer'] %}
        CAST(JSON_EXTRACT(team_attributes, '$.{{ _column }}') AS integer) AS {{ _column }},
        {%- endfor %}
        {%- for _column in team_attributes_columns_by_type['text'] %}
        CAST(JSON_EXTRACT(team_attributes, '$.{{ _column }}') AS text) AS {{ _column }},
        {%- endfor %}
        {%- for _column in team_attributes_columns_by_type['date'] %}
        CAST(DATE(CAST(JSON_EXTRACT(team_attributes, '$.{{ _column }}') AS text)) AS text) AS {{ _column }}{{ ',' if not loop.last }}
        {%- endfor %}
    FROM {{ source('Fifadata','Team_Attributes') }}
)
,
team_joined_with_team_attributes AS (
    SELECT
        team.team_long_name,
        team.team_short_name,
        {%- for _column in team_attributes_columns %}
        team_attributes.{{ _column }}{{ ',' if not loop.last }}
        {%- endfor %}
    FROM team_attributes
        INNER JOIN team ON team_attributes.team_api_id = team.team_api_id
)
,
replicated_ones AS (
    SELECT * FROM team_joined_with_team_attributes
    WHERE
        team_fifa_api_id IN (
            301,
            111429,
            111560
        )
    ORDER BY date DESC
)

SELECT * FROM replicated_ones
-- as you can see, there are replicated atributes for the same team with the same date,
-- but with the same team_fifa_api_id.
