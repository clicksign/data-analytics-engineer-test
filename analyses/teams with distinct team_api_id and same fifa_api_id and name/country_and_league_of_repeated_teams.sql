WITH team as ( -- noqa: PRS
    SELECT
        team_api_id,
        team_long_name,
        team_short_name
    FROM {{ source('Fifadata', 'Team') }}
)
,
match as (
    SELECT
        home_team_api_id,
        country_id
    FROM {{ source('Fifadata','Match') }}
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
select distinct * from team_joined_with_country where team_api_id in (8024,8020,8244,8031,9996,274581)
-- they are from the same country and league
