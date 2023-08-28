WITH team as ( -- noqa: PRS
    SELECT
        team_api_id,
        team_fifa_api_id,
        team_long_name,
        team_short_name
    FROM {{ ref('stg_team') }}
)
,
match as (
    SELECT
        home_team_api_id,
        country_id
    FROM {{ ref('stg_match') }}
)
,
league_country as (
    SELECT
        country_id,
        country_name,
        league_id,
        league_name
    FROM {{ ref('int_league_joined_with_country') }}
)
,
match_joined_country as (
    SELECT
        match.home_team_api_id,
        match.country_id,
        league_country.country_name,
        league_country.league_id,
        league_country.league_name
    FROM match
        LEFT JOIN league_country
        ON match.country_id = league_country.country_id
)
,
team_joined_with_country as (
    SELECT DISTINCT
        team.team_api_id,
        team.team_fifa_api_id,
        team.team_long_name,
        team.team_short_name,
        match_joined_country.country_id,
        match_joined_country.country_name,
        match_joined_country.league_id,
        match_joined_country.league_name
    FROM team
        LEFT JOIN match_joined_country
        ON team.team_api_id = match_joined_country.home_team_api_id
)

SELECT * FROM team_joined_with_country
