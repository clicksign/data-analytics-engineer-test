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

SELECT
    {%- for _column in _columns %}
    JSON_EXTRACT(team_attributes, '$.{{ _column }}') AS {{ _column }}{{ ',' if not loop.last }}
    {%- endfor %}
FROM {{ ref('stg_team_attributes') }}
