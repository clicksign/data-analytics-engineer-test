-- COMMAND LINE:
-- sqlite3 test_analytics_engineer.db

-- Views don't need to be updated. As soon as the tables are updated, so will the view be

-- Create view with average home team and away team goals, and preferred foot counts
CREATE VIEW FIFA_Metrics AS
WITH average_team_goals AS (
    SELECT AVG(home_team_goal) AS avg_home_team_goals, 
    AVG(away_team_goal) AS avg_away_team_goals
    FROM Match
), 
preferred_foot_right AS(
    SELECT COUNT(*) AS count_preferred_foot_right
    FROM Player_Attributes_Modified
    WHERE preferred_foot = "right"
),
preferred_foot_left AS(
    SELECT COUNT(*) AS count_preferred_foot_left
    FROM Player_Attributes_Modified
    WHERE preferred_foot = "left"
) 
SELECT avg_home_team_goals, 
avg_away_team_goals, 
count_preferred_foot_right, 
count_preferred_foot_left 
FROM average_team_goals
CROSS JOIN preferred_foot_right
CROSS JOIN preferred_foot_left;

-- View selection
SELECT * FROM FIFA_Metrics;
