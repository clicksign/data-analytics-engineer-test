-- COMMAND LINE:
-- sqlite3 test_analytics_engineer.db

-- Create Relations Table
CREATE TABLE Relations AS 
SELECT m.*, l.name AS league_name, c.name AS country_name, ta.*, p.* 
FROM League l
INNER JOIN Country c
ON l.country_id = c.id
INNER JOIN Match m
ON m.country_id = c.id
INNER JOIN Team_Attributes_Modified ta
ON ta.team_api_id = m.home_team_api_id
INNER JOIN Player p
ON m.home_player_1 = p.player_api_id;

-- Select first 10 lines
SELECT * 
FROM Relations 
LIMIT 10;

-- group by height and weight, get metrics from top 6 groups
SELECT height, 
    weight, 
    COUNT(*) AS count, 
    AVG(home_team_goal) AS avg_team_goals, 
    AVG(chanceCreationPassing) AS avg_team_chance_creation_passing
FROM Relations
GROUP BY height, weight 
ORDER BY count DESC LIMIT 6;


-- group by height, weight, country and league, get metrics from top 6 groups
SELECT height, 
    weight, 
    country_name,
    league_name,
    COUNT(*) AS count, 
    AVG(home_team_goal) AS avg_team_goals, 
    AVG(chanceCreationPassing) AS avg_team_chance_creation_passing
FROM Relations
GROUP BY height, weight, country_name, league_name 
ORDER BY count DESC LIMIT 20;