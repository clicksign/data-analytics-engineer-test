WITH playerstats AS (
    SELECT
        player_api_id AS player_id,
        height,
        weight,
        AVG(overall_rating) AS avg_performance
    FROM {{ ref('int_player_attributes_modified') }}
    WHERE overall_rating IS NOT NULL
    GROUP BY
        player_id, height, weight
)
,
playerstatsminmax AS (
    SELECT
        MIN(height) AS min_height,
        MAX(height) AS max_height,
        MIN(weight) AS min_weight,
        MAX(weight) AS max_weight
    FROM
        playerstats
)
,
playerstatsinterval AS (
    SELECT
        max_height - min_height AS height_interval,
        max_weight - min_weight AS weight_interval
    FROM
        playerstatsminmax
)
,
playerstatscategories AS (
    SELECT
        ps.player_id,
        ps.avg_performance,
        CASE
            WHEN ps.height BETWEEN psmm.min_height AND (psmm.min_height + psi.height_interval / 3) THEN 'short'
            WHEN ps.height BETWEEN (psmm.min_height + psi.height_interval / 3) AND (psmm.min_height + 2 * psi.height_interval / 3) THEN 'medium'
            ELSE 'tall'
        END AS height_category,
        CASE
            WHEN ps.weight BETWEEN psmm.min_weight AND (psmm.min_weight + psi.weight_interval / 3) THEN 'light'
            WHEN ps.weight BETWEEN (psmm.min_weight + psi.weight_interval / 3) AND (psmm.min_weight + 2 * psi.weight_interval / 3) THEN 'medium'
            ELSE 'heavy'
        END AS weight_category
    FROM
        playerstats AS ps, playerstatsinterval AS psi, playerstatsminmax AS psmm
)

SELECT * FROM playerstatscategories ORDER BY avg_performance DESC
