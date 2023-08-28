SELECT
    CASE
        WHEN preferred_foot = 'left' THEN 'Left-Footed'
        WHEN preferred_foot = 'right' THEN 'Right-Footed'
        ELSE 'Unknown'
    END AS foot_preference,
    COUNT(*) AS count
FROM {{ ref('stg_player_attributes') }}
GROUP BY foot_preference
