{%- set _columns = ['id', 'team_fifa_api_id', 'team_api_id', 'date', 'buildUpPlaySpeed',
                    'buildUpPlaySpeedClass', 'buildUpPlayDribbling',
                    'buildUpPlayDribblingClass', 'buildUpPlayPassing',
                    'buildUpPlayPassingClass', 'buildUpPlayPositioningClass',
                    'chanceCreationPassing', 'chanceCreationPassingClass',
                    'chanceCreationCrossing', 'chanceCreationCrossingClass',
                    'chanceCreationShooting', 'chanceCreationShootingClass',
                    'chanceCreationPositioningClass', 'defencePressure',
                    'defencePressureClass', 'defenceAggression', 'defenceAggressionClass',
                    'defenceTeamWidth', 'defenceTeamWidthClass', 'defenceDefenderLineClass'] %}

WITH team_attributes AS (
    SELECT
        {%- for _column in _columns %}
        JSON_EXTRACT(team_attributes, '$.{{ _column }}') AS {{ _column }}{{ ',' if not loop.last }}
        {%- endfor %}
    FROM {{ ref('stg_team_attributes') }}
)
,
team AS (
    SELECT
        id,
        team_api_id,
        team_fifa_api_id,
        team_long_name,
        team_short_name
    FROM {{ ref('stg_team') }}
)
,
team_attributes_joined_with_team AS (
    SELECT
        team.team_long_name,
        team.team_short_name,
        {%- for _column in _columns %}
        team_attributes.{{ _column }}{{ ',' if not loop.last }}
        {%- endfor %}
    FROM team_attributes
        INNER JOIN team ON team_attributes.team_api_id = team.team_api_id
)

SELECT * FROM team_attributes_joined_with_team
